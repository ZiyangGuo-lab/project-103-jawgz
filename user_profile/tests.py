from django.test import TestCase
from user_profile.models import Rider
from .forms import *
from find.models import Posting
from datetime import datetime as dt


class userProfileTest(TestCase):

    def test_valid_form(self):
        "Asserts that form is valid with provided attributes."

        form1 = update_profile_form(data ={
            "cellphone": "123456789",
            "car_type": "Test Car",
            "license_plate": "Test-123"
        })
        self.assertTrue(form1.is_valid())

    def test_not_valid1(self):
        "Asserts that form is invalid with missing attributes."

        form1 = update_profile_form(data={
            "cellphone": "123456789",
            "car_type": "Test Car",
            "license_plate": ""
        })
        self.assertFalse(form1.is_valid())

    def test_not_valid2(self):
        "Asserts that form is invalid with missing attributes."

        form1 = update_profile_form(data={
            "cellphone": "123456789",
            "car_type": "",
            "license_plate": "123"
        })
        self.assertFalse(form1.is_valid())

    def test_not_valid3(self):
        "Asserts that form is invalid with missing attributes."
        form1 = update_profile_form(data={
            "cellphone": "",
            "car_type": "Test Car",
            "license_plate": "123"
        })
        self.assertFalse(form1.is_valid())

    def test_save_rider(self):
        "Validates the ability to create and save a Rider's attributes."
        rider1 = Rider.objects.create(username="username1", license_plate="XYZ-1234", car_type="model1", cellphone="123-456-7890")
        rider1.save()

        self.assertEqual(rider1.username,"username1")
        self.assertEqual(rider1.license_plate, "XYZ-1234")
        self.assertEqual(rider1.car_type, "model1")
        self.assertEqual(rider1.cellphone, "123-456-7890")

    def test_access_accepted_rides(self):
        "Validates that rides that have been accepted appear in 'Passenger'"

        posting = Posting.objects.create(driver_name="Yuxin Wu", location_to="Charlottesville,VA",
                                    location_from="Fairfax,VA", date=dt.now(), riding_date=dt.now(), price=20,
                                    driver_id="yw7vv", num_passengers=3)
        posting.save()
        rider1 = Rider.objects.create(username="username1", license_plate="XYZ-1234", car_type="model1",
                                      cellphone="123-456-7890", rides_passenger="posting1")
        rider1.save()
        allRides = {}

        ridesPassengerIds = str(Rider.objects.filter(username=rider1)[0].rides_passenger).split(",")
        for ride in ridesPassengerIds:
            query = Rider.objects.filter(rides_passenger="posting1")
            if query.count() > 0:
                allRides[query[0]] = 'accepted'

        self.assertEqual(allRides, {rider1: 'accepted'})

    def test_access_declined_rides(self):
        "Validates that rides that have been declined appear in 'Passenger'"

        posting1 = Posting.objects.create(driver_name="Yuxin Wu", location_to="Charlottesville,VA",
                                    location_from="Fairfax,VA", date=dt.now(), riding_date=dt.now(), price=20,
                                    driver_id="yw7vv", num_passengers=3)
        posting1.save()
        rider1 = Rider.objects.create(username="username1", license_plate="XYZ-1234", car_type="model1",
                                      cellphone="123-456-7890", rides_passenger="posting1,")
        rider1.save()
        allRides = {}

        ridesPassengerIds = str(Rider.objects.filter(username=rider1)[0].rides_passenger).split(",")
        for ride in ridesPassengerIds:
            query = Rider.objects.filter(rides_declined="posting1,")
            if query.count() > 0:
                allRides[query[0]] = 'declined'

        self.assertEqual(allRides, {rider1: 'declined'})

    def test_access_pending_rides(self):
        "Validates that rides that are pending appear in 'Passenger'"

        posting1 = Posting.objects.create(driver_name="Yuxin Wu", location_to="Charlottesville,VA",
                                    location_from="Fairfax,VA", date=dt.now(), riding_date=dt.now(), price=20,
                                    driver_id="yw7vv", num_passengers=3)
        posting1.save()
        rider1 = Rider.objects.create(username="username1", license_plate="XYZ-1234", car_type="model1",
                                      cellphone="123-456-7890", rides_pending="posting1,")
        rider1.save()

        allRides = {}
        ridesPassengerIds = str(Rider.objects.filter(username=rider1)[0].rides_passenger).split(",")
        for ride in ridesPassengerIds:
            query = Rider.objects.filter(rides_passenger="posting1")
            if query.count() > 0:
                allRides[query[0]] = 'pending'

        self.assertEqual(allRides, {rider1: 'pending'})





