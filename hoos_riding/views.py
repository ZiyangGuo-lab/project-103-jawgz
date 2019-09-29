from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def login(request):
    return HttpResponse('<h1>Log In Page</h1>')


def find(request):
    return HttpResponse('<h1>Find a Ride</h1>')


def post(request):
    return HttpResponse('<h1>Post a Ride</h1>')


def profile(request):
    return HttpResponse('<h1>User Profile</h1>')

