from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='user-profile'),
    path('respondToDriverRequest', views.respondToDriverRequest, name='respondToDriverRequest'),
    path('driver-view', views.switchToDriverView, name='switchToDriverView'),
    path('passenger-view', views.profile, name='switchToPassengerView'),
    path('updateRating', views.updateRating, name='updateRating'),
    path('rate-driver', views.rateDriver, name='rate-driver')
]