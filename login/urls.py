from django.urls import path

from . import views

urlpatterns = [
    path('', views.loginPage.as_view(), name='login'),
    path('enterLogin', views.enterLogin, name='enterLogin'),
]