#forms 
from django import forms
from find.models import *

class postRide(forms.ModelForm):
	class Meta:
		model = Posting
		fields = ("location_to", "location_from","price","num_passengers")

	def __init__(self, *args, **kwargs):
		super(postRide, self).__init__(*args, **kwargs)

