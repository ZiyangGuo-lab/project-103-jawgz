from django.shortcuts import render
from .forms import *
from find.models import *
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.

def post(request):
    form = postRide(request.POST)
    if form.is_valid():
        form.save()
        # print("valid form")
    print(Posting.objects.all())
    template = 'post/post_ride.html'

    context = {
        'form': form,
    }
    return render(request, template, context)
