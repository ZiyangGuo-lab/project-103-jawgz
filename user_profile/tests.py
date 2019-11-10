from django.test import TestCase
from user_profile.models import Rider
from .forms import *


class userProfileTest(TestCase):

    def test_valid_form(self):
        form1 = update_profile_form(data ={
            "cellphone": "123456789",
            "car_type": "Test Car",
            "license_plate": "Test-123"
        })
        self.assertTrue(form1.is_valid())

