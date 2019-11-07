from django.urls import path
from . import views

urlpatterns = [
    path('', views.findView.as_view(), name='find-ride'),
    path('joinRide', views.requestToJoinRide, name='joinRide')

]

