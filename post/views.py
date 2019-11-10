from django.shortcuts import render
from .forms import *
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User
import time
from datetime import datetime
from user_profile.models import Rider

# Create your views here.

def post(request):
    form = postRide(request.POST)

    if form.is_valid():
        newPost = Posting()
        newPost.driver_id = request.user
        newPost.driver_name = request.user.first_name + " " + request.user.last_name
        newPost.location_from = request.POST.get('location_from')
        newPost.location_to = request.POST.get('location_to')
        newPost.price = request.POST.get('price')
        newPost.riding_date = formatDateTime(request.POST.get('riding_date'), request.POST.get('riding_time'))
        newPost.extra_info = request.POST.get('extra_info')

        newPost.num_passengers = request.POST.get('num_passengers')
        newPost.posting_id = hash(str(datetime.now()) + str(newPost.driver_id) + str(newPost.riding_date) + str(newPost.num_passengers))
        newPost.save()

        riderposting = Rider.objects.filter(username=request.user)[0]
        riderposting.rides_driven = str(riderposting.rides_driven) + "," + str(newPost.posting_id)
        riderposting.save()


        # form.save()
        template = 'find/find_ride.html'
        context = {
        'postings_list': Posting.objects.all()
        }

        return render(request, template,context)

    else:
        print("form is invalid")
        print(form.errors)
        context = {'form': form
        }
        template = 'post/post_ride.html'
        return render(request, template, context)

def formatDateTime(date, time):
    months = ["January","February","March","April","May","June","July","August","September","October","November","December"]
    date = date.split(" ")
    formatted = date[2] + '-' + str(months.index(date[0]) + 1) + '-' + (date[1])[:-1] + ' '

    analogTime = (time.split(" ")[0]).split(":")
    hour = int(analogTime[0])
    print("the timmmmme is", time[-2:])
    if time[-2:] == 'PM' and hour < 12:
        hour += 12

    formatted += str(hour) + ":" + analogTime[1]
    return formatted