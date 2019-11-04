from django.shortcuts import render
from user_profile.models import Rider
from user_profile.forms import update_profile_form
from find.models import Posting
from datetime import date
from django.contrib.auth.models import User

# Create your views here.
def profile(request):
    id = request.user
    print(id)
    current_user = Rider.objects.filter(username=id)
    all_rides = Posting.objects.filter(driver_id=id)
    open_rides = Posting.objects.filter(driver_id=id)
    past_rides = Posting.objects.filter(driver_id=id)
    return render(request, 'user_profile/profile.html', {'title': 'Profile', 'id': id, 'current_user': current_user,
                                                         'open_rides': open_rides, 'past_rides': past_rides})


def updateProfile(request):
    print(request)
    form = update_profile_form(request.POST)
    if form.is_valid():
        print('valid form')
    current_user = Rider.objects.filter(username=id)

    current_user.cellphone = request.POST.get('cellphone')
    current_user.car_type = request.POST.get('car_type')
    current_user.license_plate = request.POST.get('license_plate')
    current_user.save()

    print("current: ", current_user)
    return render(request, 'user_profile/profile.html', {'title': 'Profile', 'id': id, 'current_user': current_user})
