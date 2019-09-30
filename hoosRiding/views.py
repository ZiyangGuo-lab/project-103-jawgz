from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.


def login(request):
    return render(request, 'hoosRiding/login.html', {'title': 'Login'})


def find(request):
    return render(request, 'hoosRiding/find_ride.html', {'title': 'Find'})


def post(request):
    return render(request, 'hoosRiding/post_ride.html', {'title': 'Post'})


def profile(request):
    return render(request, 'hoosRiding/profile.html', {'title': 'Profile'})

