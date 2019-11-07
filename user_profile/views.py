from django.shortcuts import render
from user_profile.models import Rider
from user_profile.forms import update_profile_form
from find.models import Posting
from datetime import date
from django.contrib.auth.models import User

# Create your views here.
def profile(request):
    id = request.user
    user_matches = Rider.objects.filter(username=id)
    current_user = user_matches[0]
    # check that each field is not blank before updating
    if (request.GET.get('license_plate') is not None):
        current_user.license_plate = request.GET.get('license_plate')
        current_user.save()
    if (request.GET.get('cellphone') is not None):
        current_user.cellphone = request.GET.get('cellphone')
        current_user.save()
    if (request.GET.get('car_type') is not None):
        current_user.car_type = request.GET.get('car_type')
        current_user.save()

    all_rides = Posting.objects.filter(driver_id=id)
    open_rides = Posting.objects.filter(driver_id=id)
    past_rides = Posting.objects.filter(driver_id=id)
    return render(request, 'user_profile/profile.html', {'title': 'Profile', 'id': id, 'current_user': current_user,
                                                         'open_rides': open_rides, 'past_rides': past_rides})
