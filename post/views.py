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
        # print("hereeee")
        # newPosting = Posting()
        # newPosting.location_to = form['location_to']
        # newPosting.location_from = form['location_from']
        # newPosting.driver_name = form['driver_name']
        # newPosting.price = form['price']
        # newPosting.vehicle_model = form['vehicle_model']

        # newPosting.driver_id = int(round(time.time() * 1000))
        # newPosting.uid = str(hash(str(newPosting.driver_id) + str(newPosting.location_to) + str(newPosting.location_from)))
        # newPosting.save()
        form.save()
        # print("valid form")
    # print(Posting.objects.all())
    template = 'post/post_ride.html'

    context = {
        'form': form,
    }
    return render(request, template, context)
