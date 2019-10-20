from django.shortcuts import render
from .forms import *
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User
import time

# Create your views here.

avalible_cities = {'Charlottesville': 'VA', 'Fairfax': 'VA', 'Richmond': 'VA', 'Danville': 'VA',
                       'Virginia Beach': 'VA', 'Norfolk': 'VA', 'Alexandria': 'VA',
                       'Lynchburg': 'VA', 'Charlotte': 'NC', 'Raleigh': 'NC', 'Greensboro': 'NC', 'Newark': 'NJ',
                       'Jersey City': 'NJ', 'New York City': 'NY'}

def post(request):
    form = postRide(request.POST)

    if form.is_valid():
        print("form is valid")

        newPost = Posting()
        newPost.driver_id = request.user
        newPost.driver_name = request.user.first_name + " " + request.user.last_name
        newPost.location_from = request.POST.get('location_from')
        newPost.location_to = request.POST.get('location_to')
        newPost.price = request.POST.get('price')
        newPost.vehicle_model = request.POST.get('vehicle_model')
        newPost.date = getValidDate(request.POST)
        newPost.num_passengers = request.POST.get('num_passengers')
        newPost.save()



        # form.save()
        template = 'find/find_ride.html'
        context = {
        'postings_list': Posting.objects.all()
        }

        return render(request, template,context)

    else:
        print("form is invalid")
        print(form.errors)
        context = {'form': form,
                    'cities': avalible_cities,
        }
        template = 'post/post_ride.html'
        return render(request, template, context)

def getValidDate(data):
    str = data.get('date_year') + '-' + data.get('date_month') + "-" + data.get('date_day') + " "
    if data.get('date_time_of_day') == 'AM':
        str += data.get('date_hour')
    else:
        str += str(int(data.get('date_hour')) + 12)

    str += ":" + data.get('date_min')
    return str

