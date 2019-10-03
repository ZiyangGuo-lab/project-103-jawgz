from django.shortcuts import render
from .models import Posting
from django.views import generic

# def find(request):
#     return render(request, 'find/find_ride.html', {'title': 'Find'})

class findView(generic.ListView):
    template_name = 'find/find_ride.html'
    context_object_name = 'postings_list'

    def get_queryset(self):
        return Posting.objects.all()