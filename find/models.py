from django.db import models
from datetime import datetime, timedelta

def default_datetime():
    return datetime.now() - timedelta(hours=5)

class Posting(models.Model):
    driver_name = models.CharField(max_length=200)
    location_to = models.CharField(max_length=200)
    location_from = models.CharField(max_length=200)
    date = models.DateTimeField(default=default_datetime)
    riding_date = models.DateTimeField(default=default_datetime)
    price = models.IntegerField(default=0)
    driver_id = models.CharField(max_length=200)
    num_passengers = models.IntegerField(default=0)
    extra_info = models.TextField(null=True, blank=True)

    ratable_by = models.TextField(default=",")

    riders_requested = models.TextField()
    riders_riding = models.TextField()
    posting_id = models.CharField(max_length=200)

    def __str__(self):
        return self.driver_name