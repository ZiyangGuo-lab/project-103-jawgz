from django.shortcuts import render
from .models import Posting
from django.views import generic
from datetime import datetime
from django.http import HttpResponseRedirect
from user_profile.models import Rider
from django.contrib.auth.models import User
import datetime
from django.db.models import Q
from django.contrib.postgres.search import SearchVector

def find(request):
	return render(request, 'find/find_ride.html', {'title': 'Profile', 'postings_list' : Posting.objects.all().order_by('-date')})


def sortByRidingDate(request):
	return render(request, 'find/find_ride.html',
				  {'title': 'Profile', 'postings_list': Posting.objects.all().order_by('-riding_date')})

def sortByPrice(request):
	return render(request, 'find/find_ride.html',
				  {'title': 'Profile', 'postings_list': Posting.objects.all().order_by('-price')})

def search(request):

	all = Posting.objects.all().order_by('-date')
	print(all)
	location_to = request.POST['searchTo']
	print("to:", location_to)
	if location_to != None and location_to != '':
		if (len(location_to) > 5 and location_to[-5:] == ", USA"):
			location_to = location_to[:-5]

		filtered = []
		for posting in all:
			print(posting)
			if posting.location_to == location_to:
				filtered.append(posting)
		all = filtered

	location_from = request.POST['searchFrom']
	if location_from != None and location_from != '':
		if (len(location_from) > 5 and location_from[-5:] == ", USA"):
			location_from = location_from[:-5]

		filtered = []
		for posting in all:
			if posting.location_from == location_from:
				filtered.append(posting)
		all = filtered

	riding_date = request.POST['riding_date']
	if riding_date != None and riding_date != '':

		riding_date = formatDate(riding_date)
		print("formatted:", riding_date)
		filtered = []
		for posting in all:
			print(len(str(str(posting.riding_date).split(" ")[0])) , len(str(riding_date)))
			if str(str(posting.riding_date).split(" ")[0]) == str(riding_date):
				filtered.append(posting)
		all = filtered

	return render(request, 'find/find_ride.html',
				  {'title': 'Profile', 'postings_list': all})
		

#called when rider requesting to join posting
def requestToJoinRide(request):

    query = Posting.objects.filter(posting_id=request.GET['id'])
    if query.count() > 0 :
        posting = Posting.objects.filter(posting_id=request.GET['id'])[0]
        posting.riders_requested = str(posting.riders_requested) + "," + str(request.user)
        posting.save()

        user = Rider.objects.filter(username=str(request.user))[0]
        user.rides_pending += request.GET['id'] + ","
        user.save()

    return HttpResponseRedirect('/')

#takes in date in format: November 1, 2019, returns format: 2019-11-1
def formatDate(date):
	months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
			  "November", "December"]
	date = date.split(" ")
	return date[2] + '-' + str(months.index(date[0]) + 1) + '-' + (date[1])[:-1]


class findView(generic.ListView):
	template_name = 'find/find_ride.html'
	context_object_name = 'postings_list'
	def get_queryset(self):
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


class searchView(generic.ListView):
	model = Posting
	template_name = 'find/find_ride_search.html'
	context_object_name = 'postings_list'
	# queryset = Posting.objects.filter(location_to='Virginia Beach, VA')

	def get_queryset(self):
		location_to = self.request.GET.get('location_to')
		print(self.request.GET.get('location_to')+"location_to")
		location_from = self.request.GET.get('location_from')
		year = self.request.GET.get('date_year')
		month = self.request.GET.get('date_month')
		day = self.request.GET.get('date_day')

		s = year+ '-' +month+ '-' +day
		if location_to=="" and location_from != "" and s!="--":
			return Posting.objects.filter(location_from=location_from, riding_date__date=s)
		elif location_to!="" and location_from == "" and s!="--":
			return Posting.objects.filter(location_to=location_to, riding_date__date=s)
		elif location_to!="" and location_from != "" and s=="--":
			return Posting.objects.filter(location_to=location_to, location_from=location_from)
		elif location_to=="" and location_from == "" and s!="--":
			return Posting.objects.filter(riding_date__date=s)
		elif location_to !="" and location_from == "" and s=="--":
			print("method goes here")
			return Posting.objects.filter(location_to=location_to)
		elif location_to =="" and location_from != "" and s=="--":
			return Posting.objects.filter(location_from=location_from)
		elif location_to =="" and location_from == "" and s=="--":
			return Posting.objects.filter(location_from=location_from)
		else:
			return Posting.objects.filter(location_to=location_to, location_from=location_from, riding_date__date=s)



