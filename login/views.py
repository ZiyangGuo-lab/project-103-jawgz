from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views import generic
from django.views.generic import CreateView
from .models import User
from django.http import HttpResponseRedirect
from django.contrib.auth import logout

class loginPage(CreateView):
    model = User
    fields = ('username', 'password')
    template_name = 'login.html'


def enterLogin(request):
    if(request.method == 'GET'):
        print("here with " + request.GET['username'] + " " + request.GET['password'])
        query = User.objects.filter(username=request.GET['username'], password=request.GET['password'])
        if(query.count() > 0):
            match = query[0]
            print("found match!" + "\nname: " + match.name + "\nusername: " + match.username + "\npassword " + match.password)
        else:
            print("no match found...")
        return HttpResponseRedirect('/login')

    elif request.method == 'POST':
        newUser = User()
        newUser.name = request.POST['name']
        newUser.username = request.POST['username']
        newUser.password = request.POST['password']
        newUser.save()

        return HttpResponseRedirect('/login')

def userLogOut(request):
    print(request.user.first_name)
    logout(request)
    return HttpResponseRedirect('/login')

