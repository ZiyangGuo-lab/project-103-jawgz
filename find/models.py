from django.db import models


class Posting(models.Model):
    driver_name = models.CharField(max_length=200)
    vehicle_model = models.CharField(max_length=200)
    location_to = models.CharField(max_length=200)
    location_from = models.CharField(max_length=200)
    time = models.CharField(max_length=200)

    def __str__(self):
        return self.driver_name