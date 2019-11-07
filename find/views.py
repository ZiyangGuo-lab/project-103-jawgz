from django.shortcuts import render
from .models import Posting
from django.views import generic
from datetime import datetime
from django.http import HttpResponseRedirect
from user_profile.models import Rider

class findView(generic.ListView):
    template_name = 'find/find_ride.html'
    context_object_name = 'postings_list'

    def get_queryset(self):
        return Posting.objects.all()



def requestToJoinRide(request):
    print("id of posting: " + request.GET['id'])

    print(Posting.objects.filter(posting_id=request.GET['id'])[0].driver_name)

    query = Posting.objects.filter(posting_id=request.GET['id'])
    if query.count() > 0 :
        posting = Posting.objects.filter(posting_id=request.GET['id'])[0]
        posting.riders_requested = str(posting.riders_requested) + "," + str(request.user)
        posting.save()

        user = Rider.objects.filter(username=str(request.user))[0]
        user.rides_pending += request.GET['id'] + ","
        user.save()

    return HttpResponseRedirect('/')

# def order_by_date(request):
#     posting = Posting()
#     return Posting.objects.filter(
#         pub_date__lte=datetime.now()
#     ).order_by('-date')