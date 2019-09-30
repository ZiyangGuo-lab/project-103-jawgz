from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.


def login(request):
    return render(request, 'hoosRiding/login.html')


def find(request):
    return render(request, 'hoosRiding/find_ride.html')


def post(request):
    return render(request, 'hoosRiding/post_ride.html')


def profile(request):
    return render(request, 'hoosRiding/profile.html')

