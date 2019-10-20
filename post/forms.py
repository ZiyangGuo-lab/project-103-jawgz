#forms 
from django import forms
from find.models import *

class postRide(forms.ModelForm):
	class Meta:
		model = Posting
		fields = ("location_to", "location_from","vehicle_model","price","num_passengers")
		# fields = ("location_to", "location_from","driver_name", "vehicle_model","price")

	def __init__(self, *args, **kwargs):
		super(postRide,self).__init__(*args, **kwargs)

# class NameForm(forms.Form):
#     your_name = forms.CharField(label='Your name', max_length=100)