from django.urls import path
from . import views

urlpatterns = [
    path('', views.findView.as_view(), name='find-ride'),
    # path('', views.findRide, name='find-ride'),
    path('sortByPrice', views.priceView.as_view(), name='sortByPrice'),
    path('sortByDate', views.dateView.as_view(), name='sortByDate'),
    path('search', views.searchView.as_view(), name='search')
]

