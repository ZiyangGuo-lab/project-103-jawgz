from django.db import models
from datetime import datetime, timedelta
from django.contrib.auth.models import User


def default_datetime():
    return datetime.now() + timedelta(days=1)

class Posting(models.Model):
    driver_name = models.CharField(max_length=200)
    vehicle_model = models.CharField(max_length=200)
    location_to = models.CharField(max_length=200)
    location_from = models.CharField(max_length=200)
    date = models.DateTimeField(default=default_datetime)
    price = models.IntegerField(default = 0)
    riding_date = models.DateTimeField(default=default_datetime)
    driver_id = models.CharField(max_length=200)
    num_passengers = models.IntegerField(default=0)

    def __str__(self):
        return self.driver_name