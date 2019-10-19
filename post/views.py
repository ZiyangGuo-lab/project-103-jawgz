from django.shortcuts import render
from .forms import *
from find.models import *
from django.http import HttpResponseRedirect
from django.shortcuts import render
import time

# Create your views here.

avalible_cities = {'Charlottesville': 'VA', 'Fairfax': 'VA', 'Richmond': 'VA', 'Danville': 'VA',
                       'Virginia Beach': 'VA', 'Norfolk': 'VA', 'Alexandria': 'VA',
                       'Lynchburg': 'VA', 'Charlotte': 'NC', 'Raleigh': 'NC', 'Greensboro': 'NC', 'Newark': 'NJ',
                       'Jersey City': 'NJ', 'New York City': 'NY'}

def post(request):
    form = postRide(request.POST)
    form.location_from = request.POST.get('location_from')
    form.location_to = request.POST.get('location_to')
    print(form.errors)

    filter_by = forms.ChoiceField(choices=FILTER_CHOICES)

    if form.is_valid():
        print("form is valid")
        form.save()
        template = 'find/find_ride.html'
        context = {
        'postings_list': Posting.objects.all()
        }

        return render(request, template,context)

    else:

        context = {'form': form,
                    'cities': avalible_cities,
                   'filter_by' : filter_by
        }
        template = 'post/post_ride.html'
        return render(request, template, context)


