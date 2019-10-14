#forms 
from django import forms
from .models import *

class postRide(forms.ModelForm):
	class Meta:
		model = Posting
		fields = ("location_to", "location_from","driver_name", "vehicle_model","date","price")
		

# class NameForm(forms.Form):
#     your_name = forms.CharField(label='Your name', max_length=100)