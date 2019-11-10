from django.shortcuts import render
from django.contrib.auth.models import User

from user_profile.models import Rider
from find.models import Posting
from django.http import HttpResponseRedirect

# Create your views here.
def profile(request):
    id = request.user
    user_matches = Rider.objects.filter(username=id)
    current_user = user_matches[0]
    #check if modal form has been filled out yet
    if (request.GET.get('license_plate') is not None):
        current_user.license_plate = request.GET.get('license_plate')
        current_user.save()
    if (request.GET.get('cellphone') is not None):
        current_user.cellphone = request.GET.get('cellphone')
        current_user.save()
    if (request.GET.get('car_type') is not None):
        current_user.car_type = request.GET.get('car_type')
        current_user.save()
    allRides = {}
    ridesPassengerIds = str(Rider.objects.filter(username=request.user)[0].rides_passenger).split(",")
    for ride in ridesPassengerIds:
        query = Posting.objects.filter(posting_id=ride)
        if query.count() > 0:
            allRides[query[0]] = 'accepted'

    ridesPendingIds = str(Rider.objects.filter(username=request.user)[0].rides_pending).split(",")
    for ride in ridesPendingIds:
        query = Posting.objects.filter(posting_id=ride)
        if query.count() > 0:
            allRides[query[0]] = 'pending'

    ridesDeclinedIds = str(Rider.objects.filter(username=request.user)[0].rides_declined).split(",")
    for ride in ridesDeclinedIds:
        query = Posting.objects.filter(posting_id=ride)
        if query.count() > 0:
            allRides[query[0]] = 'declined'

    print(allRides)

    return render(request, 'user_profile/profile.html', {'title': 'Profile', 'id': id, 'current_user': current_user,
                                                         'allRides': allRides, 'viewingPassenger': True})


#method called when driver accepts or declines a new passenger
def respondToDriverRequest(request):

    postingObject = Posting.objects.filter(posting_id=request.GET['id'])[0]
    passenger = Rider.objects.filter(username=request.GET['rider'])[0]

    #if passenger is accepted
    if(request.GET['status'] == "accept"):
        postingObject.riders_riding += passenger.username + "," #add to riders riding
        postingObject.num_passengers -= 1
        passenger.rides_passenger += request.GET['id'] + "," #update rider's info to save is riding
        passenger.save()
    else:
        passenger.rides_declined += request.GET['id'] + "," # update rider's info, ride declined
        passenger.save()

    #remove from posting
    requested = postingObject.riders_requested
    postingObject.riders_requested = requested[:requested.index(passenger.username)] + requested[requested.index(passenger.username)+len(passenger.username):]
    postingObject.save()

    #remove from passenger
    pending = passenger.rides_pending
    passenger.rides_pending = pending[:pending.index(request.GET['id'])] + pending[pending.index(request.GET['id']) + len(request.GET['id']):]
    print("passenger pending: " + passenger.rides_pending)
    passenger.save()

    return switchToDriverView(request)


def switchToDriverView(request):
    id = request.GET.get('user')
    ridesDrivingIds = str(Rider.objects.filter(username=request.user)[0].rides_driven).split(",")
    ridesDriving = []
    for ride in ridesDrivingIds:
        query = Posting.objects.filter(posting_id=ride)
        if query.count() > 0:
            ridesDriving.append(query[0])

    return render(request, 'user_profile/profile.html',
                  {'title': 'Profile', 'id': id, 'ridesDriving': ridesDriving, 'viewingPassenger': False})