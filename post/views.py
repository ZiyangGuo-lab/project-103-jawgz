from django.shortcuts import render
from .forms import *
from find.models import *
from django.http import HttpResponseRedirect
from django.shortcuts import render
import time

# Create your views here.

def post(request):
    form = postRide(request.POST)
    
    if form.is_valid():
        form.save()
        # print(form['location_to'])
        # print("valid form")
    # print(Posting.objects.all())
        template = 'find/find_ride.html'
        context = {
        'postings_list': Posting.objects.all()
        }

        return render(request, template,context)
    else:
        context = {'form': form,
        }
        template = 'post/post_ride.html'
        return render(request, template, context)


