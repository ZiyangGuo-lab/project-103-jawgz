from django.shortcuts import render
from .models import Posting
from django.views import generic
from datetime import datetime

# def find(request):
#     return render(request, 'find/find_ride.html', {'title': 'Find'})

class findView(generic.ListView):
    template_name = 'find/find_ride.html'
    context_object_name = 'postings_list'

    def get_queryset(self):
        return Posting.objects.all()


# def order_by_date(request):
#     posting = Posting()
#     return Posting.objects.filter(
#         pub_date__lte=datetime.now()
#     ).order_by('-date')