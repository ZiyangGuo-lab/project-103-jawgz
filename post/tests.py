from django.test import TestCase
from .forms import *
from find.models import *
from django.contrib.auth.models import User


# Create your tests here.
class postRideTest(TestCase):

	def test_form_validation(self):
		form1 = postRide(data = {
			"location_to" : " Charlottesville, VA", 
			"location_from": "FairFax, VA", 
			"vehicle_model": "Honda",
			"price" : 20, 
			"num_passengers": 2, 
			})
		form2 = postRide(data = {
			"location_to" : " Charlottesville, VA", 
			"location_from": "FairFax, VA",
			"vehicle_model": "",
			"price" : 20, 
			"num_passengers": 2,  
			})

		self.assertFalse(form2.is_valid())
		self.assertTrue(form1.is_valid())

	def test_form_empty(self):
		form1 = postRide(data = {
			"location_to" : " Charlottesville, VA", 
			"location_from": "FairFax, VA",
			"vehicle_model": "",
			"price" : 20, 
			"num_passengers": 2, 
			})

		form2 = postRide(data = {
			"location_to" : "", 
			"location_from": "FairFax, VA", 
			"vehicle_model": "Honda",
			"price" : 20, 
			"num_passengers": 2, 
			})
		form3 = postRide(data = {
			"location_to" : "", 
			"location_from": "FairFax, VA", 
			"vehicle_model": "Honda",
			"price" : " ", 
			"num_passengers": 2, 
			})			


		self.assertFalse(form2.is_valid())
		self.assertFalse(form1.is_valid())
		self.assertFalse(form3.is_valid())

	def test_form_content(self):
		form1 = postRide(data = {
			"location_to" : "Charlottesville, VA", 
			"location_from": "FairFax, VA",
			"vehicle_model": "Honda",
			"price" : 20, 
			"num_passengers": 2,  
			})
		form1 = form1.save()

		self.assertEqual(form1.location_to, "Charlottesville, VA")
		self.assertEqual(form1.num_passengers, 2)
		self.assertEqual(form1.vehicle_model, "Honda")

	



