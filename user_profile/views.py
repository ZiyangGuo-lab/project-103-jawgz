from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.
def profile(request):
    print(request.user)
    return render(request, 'user_profile/profile.html', {'title': 'Profile'})



