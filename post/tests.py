from django.test import TestCase
from .forms import *
from find.models import *


# Create your tests here.
class postRideTest(TestCase):

	def test_form_validation(self):
		form1 = postRide(data = {
			"location_to" : " Charlottesville, VA", 
			"location_from": "FairFax, VA",
			"driver_name": "Bob", 
			"vehicle_model": "Honda",
			"price" : 20, 
			"riding_date": "2019-10-18 14:00", 
			})
		form2 = postRide(data = {
			"location_to" : " Charlottesville, VA", 
			"location_from": "FairFax, VA",
			"driver_name": "Bob", 
			"vehicle_model": "Honda",
			"price" : 20, 
			"riding_date": "2019", 
			})

		self.assertFalse(form2.is_valid())
		self.assertTrue(form1.is_valid())

	def test_form_empty(self):
		form1 = postRide(data = {
			"location_to" : " Charlottesville, VA", 
			"location_from": "FairFax, VA",
			"driver_name": "Bob", 
			"vehicle_model": "",
			"price" : 20, 
			"riding_date": "2019-10-18 14:00", 
			})
		form2 = postRide(data = {
			"location_to" : "", 
			"location_from": "FairFax, VA",
			"driver_name": "Bob", 
			"vehicle_model": "Honda",
			"price" : 20, 
			"riding_date": "2019", 
			})

		self.assertFalse(form2.is_valid())
		self.assertFalse(form1.is_valid())

	def test_form_content(self):
		form1 = postRide(data = {
			"location_to" : "Charlottesville, VA", 
			"location_from": "FairFax, VA",
			"driver_name": "Bob", 
			"vehicle_model": "Honda",
			"price" : 20, 
			"riding_date": "2019-10-18 14:00", 
			})
		form1 = form1.save()

		self.assertEqual(form1.location_to, "Charlottesville, VA")
		self.assertEqual(form1.driver_name, "Bob")



