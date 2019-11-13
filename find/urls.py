from django.urls import path
from . import views

urlpatterns = [
    path('', views.find, name='find-ride'),
    path('joinRide', views.requestToJoinRide, name='joinRide'),
    path('sortByPostingDate', views.sortByPostingDate, name='sortByPostingDate'),
    path('sortByPrice', views.sortByPrice, name='sortByPrice'),
    path('sortByRidingDate', views.sortByRidingDate, name='sortByRidingDate'),
    path('search', views.search, name='search')
]
