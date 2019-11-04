from django.shortcuts import render
from user_profile.models import Rider
from user_profile.forms import ProfileForm

from django.contrib.auth.models import User

# Create your views here.
def profile(request):
    id = request.user
    print (id)
    current_user = Rider.objects.filter(username=id)
    print(current_user)
    return render(request, 'user_profile/profile.html', {'title': 'Profile', 'id': id})



