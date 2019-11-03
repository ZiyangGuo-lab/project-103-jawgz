from django.shortcuts import render
from .models import Posting
from django.views import generic
from datetime import datetime
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
import time
from django.db.models import Q

class findView(generic.ListView):
    template_name = 'find/find_ride.html'
    context_object_name = 'postings_list'

    def get_queryset(self):
    	# print("find ride")
    	return Posting.objects.all()


class dateView(generic.ListView):
    template_name = 'find/find_ride_date.html'
    context_object_name = 'postings_list'

    def get_queryset(self):
    	# print("find ride")
    	return Posting.objects.all().order_by('-riding_date')

class priceView(generic.ListView):
    template_name = 'find/find_ride_price.html'
    context_object_name = 'postings_list'

    def get_queryset(self):
    	return Posting.objects.all().order_by('price')


# class searchView(generic.ListView):
#     template_name = 'find/find_ride_search.html'
#     context_object_name = 'postings_list'

#     def get_queryset(self):
#     	return Posting.objects.all().order_by('price')