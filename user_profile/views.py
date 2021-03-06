from django.shortcuts import render
from django.contrib.auth.models import User
from user_profile.models import Rider
from find.models import Posting
from django.http import HttpResponseRedirect
from datetime import datetime as dt
from django.core.files.storage import default_storage
from django.utils import timezone

now = timezone.now()

# method called
def calculate_rating(current_user):
    rating_array = current_user.ratings_list.split(",")  # average of rating_list
    total_rating = 0
    count = 0

    for i in range(0, len(rating_array)):
        if rating_array[i] != '':
            count += 1
            total_rating += int(rating_array[i])
    if count > 0:
        new_rating = round(total_rating / count, 2)
        current_user.rating = new_rating
    else:
        current_user.rating = 0
    current_user.save()

    return current_user.rating


def updateRating(request):
    # if posting "ratable by" contains rider's username, then don't update rating
    id = request.user
    user_matches = Rider.objects.filter(username=id)
    current_user = str(user_matches[0])
    posting = Posting.objects.filter(posting_id=request.GET['post_id'])[0]
    ratable = posting.ratable_by
    posting.ratable_by = ratable[:ratable.index(current_user)] + ratable[
                                                                 ratable.index(current_user) + len(current_user):]
    posting.save()

    # id is the driver_id and this fins the rider with the same id and updates rating
    rider_to_rate = Rider.objects.filter(username=request.GET['id'])
    rider_to_rate = rider_to_rate[0]
    rider_to_rate.ratings_list = rider_to_rate.ratings_list + ", " + str(request.GET['rating'])
    rider_to_rate.rating = calculate_rating(rider_to_rate)
    rider_to_rate.save()

    return profile(request)


# Create your views here.
def profile(request):
    id = request.user
    user_matches = Rider.objects.filter(username=id)
    if len(user_matches) == 0:
        return HttpResponseRedirect("/")
    handleForm(request)
    allRides = {}
    pastRides = {}
    futureRides = {}

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

    # calculates the rating for the current user to be displayed on profile page
    id = request.user
    user_matches = Rider.objects.filter(username=id)
    current_user = user_matches[0]
    rating = calculate_rating(current_user)

    # filter past rides
    for posting, status in allRides.items():
        # d = datetime.strptime(posting.riding_date, "%Y-%m-%d %H:%M")
        if posting.riding_date < now:
            pastRides[posting] = status
        else:
            futureRides[posting] = status

    return render(request, 'user_profile/profile.html', {'title': 'Profile', 'id': id, 'current_user': current_user,
                                                         'allRides': allRides, 'viewingPassenger': True,
                                                         'rating': rating, 'future': True, 'pastRides': pastRides,
                                                         'futureRides': futureRides})


def handleForm(request):
    id = request.user
    user_matches = Rider.objects.filter(username=id)
    current_user = user_matches[0]
    name = request.user.first_name + ' ' + request.user.last_name
    current_user.name = name
    current_user.save()
    # check if modal form has been filled out yet
    if 'image' in request.FILES:
        current_user.image = request.FILES['image']
        current_user.save()
    if request.POST.get('license_plate') is not None:
        current_user.license_plate = request.POST.get('license_plate')
        current_user.save()
    if request.POST.get('cellphone') is not None:
        current_user.cellphone = request.POST.get('cellphone')
        current_user.save()
    if request.POST.get('car_type') is not None:
        current_user.car_type = request.POST.get('car_type')
        current_user.save()
    return current_user

# method called when driver accepts or declines a new passenger
def respondToDriverRequest(request):
    postingObject = Posting.objects.filter(posting_id=request.GET['id'])[0]
    passenger = Rider.objects.filter(username=request.GET['rider'])[0]

    # if passenger is accepted
    if (request.GET['status'] == "accept"):
        postingObject.riders_riding += passenger.username + ","  # add to riders riding
        postingObject.ratable_by += passenger.username + ","
        postingObject.num_passengers -= 1
        passenger.rides_passenger += request.GET['id'] + ","  # update rider's info to save is riding
        passenger.save()
    else:
        passenger.rides_declined += request.GET['id'] + ","  # update rider's info, ride declined
        passenger.save()

    # remove from posting
    requested = postingObject.riders_requested
    postingObject.riders_requested = requested[:requested.index(passenger.username)] + requested[requested.index(
        passenger.username) + len(passenger.username):]
    postingObject.save()

    # remove from passenger
    pending = passenger.rides_pending
    passenger.rides_pending = pending[:pending.index(request.GET['id'])] + pending[
                                                                           pending.index(request.GET['id']) + len(
                                                                               request.GET['id']):]
    # print("passenger pending: " + passenger.rides_pending)
    passenger.save()

    return HttpResponseRedirect("/profile/driver-view")


def switchToDriverView(request):
    id = request.user
    current_user = handleForm(request)
    ridesDrivingIds = str(Rider.objects.filter(username=request.user)[0].rides_driven).split(",")
    ridesDriving = []
    pastRides = []
    futureRides = []

    id = request.user
    user_matches = Rider.objects.filter(username=id)
    current_user = user_matches[0]
    rating = calculate_rating(current_user)

    for ride in ridesDrivingIds:
        query = Posting.objects.filter(posting_id=ride)
        if query.count() > 0:
            ridesDriving.append(query[0])
    for posting in ridesDriving:
        if posting.riding_date < now:
            pastRides.append(posting)
        else:
            futureRides.append(posting)

    return render(request, 'user_profile/profile.html',
                  {'title': 'Profile', 'id': id, 'ridesDriving': ridesDriving, 'viewingPassenger': False,
                   'rating': rating, 'current_user': current_user, 'futureRides': futureRides, 'pastRides': pastRides})

def deleteRide(request):
    # remove ride from any Riders in postings' riders_riding
    posting = Posting.objects.filter(posting_id=request.GET['id'])[0]

    # remove ride from any Riders in postings' riders_riding
    riders_list = posting.riders_riding
    riders_array = riders_list.split(",")

    for username in riders_array:
        if username != '':
            rider = Rider.objects.filter(username=username)[0]
            riding = rider.rides_passenger
            rider.rides_passenger = riding[:riding.index(posting.posting_id)] + riding[riding.index(
                posting.posting_id) + len(posting.posting_id):]
            rider.save()

    # remove ride from any Riders in postings' riders_requested
    riders_list = posting.riders_requested
    riders_array = riders_list.split(",")

    for username in riders_array:
        if username != '':
            rider = Rider.objects.filter(username=username)[0]
            riding = rider.rides_pending
            rider.rides_pending = riding[:riding.index(posting.posting_id)] + riding[riding.index(
                posting.posting_id) + len(posting.posting_id):]
            rider.save()

    # remove ride from any Riders in postings' riders_requested
    posting.delete()


    return HttpResponseRedirect("/profile/switchToDriverView")

def removeMyself(request):
    posting = Posting.objects.filter(posting_id=request.GET['id'])[0]
    id = request.user
    user_matches = Rider.objects.filter(username=id)
    current_user = user_matches[0]
    username = current_user.username

    # remove rider from posting's riders_riding and increase number of passengers
    riding = posting.riders_riding
    if riding.find(username) > -1:
        posting.riders_riding = riding[:riding.index(username)] + riding[riding.index(
            username) + len(username):]
        posting.num_passengers += 1
        posting.save()

    # remove rider from posting's riders_requested
    requested = posting.riders_requested
    if requested.find(username) > -1:
        posting.riders_requested = requested[:requested.index(username)] + requested[requested.index(
            username) + len(username):]
        posting.save()

    # remove ride from Rider's if rides_passenger
    riding = current_user.rides_passenger
    if riding.find(posting.posting_id) > -1:
        current_user.rides_passenger = riding[:riding.index(posting.posting_id)] + riding[riding.index(
            posting.posting_id) + len(posting.posting_id):]
        current_user.save()

    # remove ride from Rider's if rides_pending
    riding = current_user.rides_pending
    if riding.find(posting.posting_id) > -1:
        current_user.rides_pending = riding[:riding.index(posting.posting_id)] + riding[riding.index(
            posting.posting_id) + len(posting.posting_id):]
        current_user.save()

    # remove ride from Rider's if rides_declined
    riding = current_user.rides_declined
    if riding.find(posting.posting_id) > -1:
        current_user.rides_declined = riding[:riding.index(posting.posting_id)] + riding[riding.index(
            posting.posting_id) + len(posting.posting_id):]
        current_user.save()

    return HttpResponseRedirect("/profile")


def rateDriver(request):
    rating = request.GET["rating"]
    user = request.user
    rideId = request.GET["ride"]
    driver = request.GET['driver']
    # print("rating a ride\nrating:",rating,"\nuser:",user,"\nride id",rideId)

    # if posting "ratable by" contains rider's username, then don't update rating
    id = request.user
    user_matches = Rider.objects.filter(username=id)
    current_user = str(user_matches[0])
    posting = Posting.objects.filter(posting_id=rideId)[0]
    ratable = posting.ratable_by
    posting.ratable_by = ratable[:ratable.index(current_user)] + ratable[ratable.index(current_user) + len(current_user):]
    posting.save()

    # id is the driver_id and this fins the rider with the same id and updates rating
    rider_to_rate = Rider.objects.filter(username=driver)
    rider_to_rate = rider_to_rate[0]
    rider_to_rate.ratings_list = rider_to_rate.ratings_list + ", " + str(rating)
    rider_to_rate.rating = calculate_rating(rider_to_rate)
    rider_to_rate.save()

    return HttpResponseRedirect("/profile")
