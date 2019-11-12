from django.test import TestCase
from .forms import *
from find.models import *
from find.views import *
from datetime import datetime as dt

import requests
from django.contrib.auth.models import User


# Create your tests here.
class postRideTest(TestCase):
	def setUp(self):
		self.form1 = postRide(data={
			"location_to": " Charlottesville, VA",
			"location_from": "FairFax, VA",
			"price": 20,
			"num_passengers": 2,
		})
		self.form2 = postRide(data={
			"location_to": " Charlottesville, VA",
			"location_from": "FairFax, VA",
			"price": 20,
			"num_passengers": 2,
			"extra_info": "car is a 2008 model",
		})

	def test_form_validation1(self):
		" Asserts that two forms are valid. "
		self.assertTrue(self.form1.is_valid())

	def test_form_validation2(self):
		self.assertTrue(self.form2.is_valid())

	def test_form_empty1(self):
		" Asserts that forms with missing values for necessary fields are not valid. "
		# missing "location_to"
		form1 = postRide(data={
			"location_to": "",
			"location_from": "FairFax, VA",
			"price": 20,
			"num_passengers": 2,
		})
		self.assertFalse(form1.is_valid())

	def test_form_empty2(self):
		# missing "location_from"
		form2 = postRide(data={
			"location_to": "Richmond, VA",
			"location_from": "",
			"price": 20,
			"num_passengers": 2,
		})
		self.assertFalse(form2.is_valid())

	def test_form_empty3(self):
		# missing "price"
		form3 = postRide(data={
			"location_to": "Richmond, VA",
			"location_from": "FairFax, VA",
			"price": "",
			"num_passengers": 2,
		})
		self.assertFalse(form3.is_valid())

	def test_form_empty3(self):
		# missing num_passengers
		form4 = postRide(data={
			"location_to": "Richmond, VA",
			"location_from": "FairFax, VA",
			"price": 5,
			"num_passengers": "",
		})
		self.assertFalse(form4.is_valid())

	def test_form_extra_empty(self):
		" Asserts that 'extra_info' can be an empty value. "
		# missing "extra_info"
		form1 = postRide(data={
			"location_to": "",
			"location_from": "FairFax, VA",
			"price": 20,
			"num_passengers": 2,
			"extra_info": "car is a 2008 model",
		})

		self.assertFalse(form1.is_valid())

	def test_form_content(self):
		" Asserts that forms saves correct attributes to Posting. "
		form1 = postRide(data={
			"location_to": "Charlottesville, VA",
			"location_from": "Fairfax, VA",
			"price": 20,
			"num_passengers": 2,
		})
		form1 = form1.save()

		self.assertEqual(form1.location_to, "Charlottesville, VA")
		self.assertEqual(form1.num_passengers, 2)
		self.assertEqual(form1.location_from, "Fairfax, VA")
		self.assertEqual(form1.price, 20)

	def test_posting_is_saved(self):
		" Once a form is submitted, number of postings increases by 1."
		startCount = Posting.objects.count()
		form1 = postRide(data={
			"location_to": "Charlottesville, VA",
			"location_from": "Fairfax, VA",
			"price": 20,
			"num_passengers": 2,
		})
		form1.save()
		endCount = Posting.objects.count()
		self.assertEqual(startCount, endCount - 1)

	def test_posting_is_saved_correctly1(self):
		" Once two forms are saved, number of postings increases by two."
		form1 = postRide(data={
			"location_to": "Charlottesville, VA",
			"location_from": "Fairfax, VA",
			"price": 20,
			"num_passengers": 2,
		})
		form2 = postRide(data={
			"location_to": "Charlottesville, VA",
			"location_from": "Fairfax, VA",
			"price": 20,
			"num_passengers": 2,
		})
		form2.save()
		form1.save()
		postings_list = Posting.objects.all()
		self.assertEqual(len(postings_list), 2)

	def test_posting_is_saved_correctly2(self):
		" Once two forms are saved, number of postings increases by one if one form is invalid."
		form1 = postRide(data={
			"location_to": "Charlottesville, VA",
			"location_from": "Fairfax, VA",
			"price": "",  # this is required
			"num_passengers": 2,
		})
		form2 = postRide(data={
			"location_to": "Charlottesville, VA",
			"location_from": "Fairfax, VA",
			"price": 20,
			"num_passengers": 2,
		})
		try:
			form1.save()
		except:
			print("form1 cannnot be saved")
		try:
			form2.save()
		except:
			print("form2 cannot be saved")
		postings_list = Posting.objects.all()
		self.assertEqual(len(postings_list), 1)

	def test_form_is_saved_correctly3(self):
		"Form is can be ordered correctly among other Postings once saved."
		price = priceView()
		form1 = postRide(data={"driver_name": "Garrett",
							   "location_to": "Charlottesville, VA",
							   "location_from": "Fairfax, VA",
							   "price": 19,
							   "num_passengers": 2,
							   })
		form1.save()
		p1 = Posting.objects.create(driver_name="Yuxin Wu", location_to="Charlottesville,VA",
									location_from="Fairfax,VA", date=dt.now(), riding_date=dt.now(), price=20,
									driver_id="yw7vv", num_passengers=3)
		p1.save()
		p2 = Posting.objects.create(driver_name="Yuxin Wu", location_to="Jersey City,NJ", location_from="Fairfax,VA",
									date=dt.now(), riding_date=dt.now(), price=1, driver_id="yw7vv", num_passengers=2)
		p2.save()
		p3 = Posting.objects.create(driver_name="Ziyang Guo", location_to="Jersey City,NJ",
									location_from="CharlottesvilleVA", date=dt.now(), riding_date=dt.now(), price=3,
									driver_id="zg2mt", num_passengers=2)
		p3.save()
		m = price.get_queryset()
		# 4th in list is p1 which has the highest price
		self.assertEqual(m[3], p1)


# def test_formatDateTime(self):
# 	" Asserts our time and date from our form are parsed correctly. "
# 	# date = "%Y-%m-%d %H:%M:%S"
# 	date = "2019-10-10"
# 	time = "10:10:10"
#
# 	print(formatDateTime(date, time))
# 	print(dt.now())


def formatDateTime(date, time):
	months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
			  "November", "December"]
	date = date.split(" ")
	formatted = date[2] + '-' + str(months.index(date[0]) + 1) + '-' + (date[1])[:-1] + ' '

	analogTime = (time.split(" ")[0]).split(":")
	hour = int(analogTime[0])
	if time[-2:] == 'PM' and hour < 12:
		hour += 12

	formatted += str(hour) + ":" + analogTime[1]
	return formatted