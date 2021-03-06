from django.shortcuts import render
from .forms import *
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User
import time
from datetime import datetime
from user_profile.models import Rider
from find.views import find

# Create your views here.

def post(request):
    form = postRide(request.POST)

    if form.is_valid():
        newPost = Posting()
        newPost.driver_id = request.user
        newPost.driver_name = request.user.first_name + " " + request.user.last_name
        #remove country name, search is restricted to USA
        location_from = request.POST.get('location_from')
        if(len(location_from) > 5 and location_from[-5:] == ", USA"):
            location_from = location_from[:-5]
        newPost.location_from = location_from

        location_to = request.POST.get('location_to')
        if (len(location_to) > 5 and location_to[-5:] == ", USA"):
            location_to = location_to[:-5]
        newPost.location_to = location_to

        newPost.price = request.POST.get('price')
        newPost.riding_date = formatDateTime(request.POST.get('riding_date'), request.POST.get('riding_time'))
        d = datetime.strptime(newPost.riding_date, "%Y-%m-%d %H:%M")
        # print(newPost.riding_date)
        # print(datetime.now())
        newPost.extra_info = request.POST.get('extra_info')
        if d <= datetime.now():
            print("form is invalid")
            print(form.errors)
            context = {'form': form, 'invalid': True
            }
            template = 'post/post_ride.html'
            return render(request, template, context)
        newPost.num_passengers = request.POST.get('num_passengers')
        newPost.posting_id = hash(str(datetime.now()) + str(newPost.driver_id) + str(newPost.riding_date) + str(newPost.num_passengers))
        newPost.save()

        riderposting = Rider.objects.filter(username=request.user)[0]
        riderposting.rides_driven = str(riderposting.rides_driven) + "," + str(newPost.posting_id)
        riderposting.save()


        # # form.save()
        # template = 'find/find_ride.html'
        # context = {
        # 'postings_list': Posting.objects.all()
        # }
        return HttpResponseRedirect('/')

    else:
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
    if time[-2:] == 'PM' and hour < 12:
        hour += 12

    formatted += str(hour) + ":" + analogTime[1]
    return formatted