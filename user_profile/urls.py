from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='user-profile'),
    path('updateProfile', views.update_profile_form, name="update-profile")
]