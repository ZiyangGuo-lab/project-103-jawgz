from django.shortcuts import render
from .forms import *
from find.models import *
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
    form.location_from = request.POST.get('location_from')
    form.location_to = request.POST.get('location_to')
    form.driver_id = str(request.user)
    print(request.user)



    if form.is_valid():
        print("form is valid")
        form.save()
        template = 'find/find_ride.html'
        context = {
        'postings_list': Posting.objects.all()
        }

        return render(request, template,context)

    else:

        context = {'form': form,
                    'cities': avalible_cities,
        }
        template = 'post/post_ride.html'
        return render(request, template, context)


