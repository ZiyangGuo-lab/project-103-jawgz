from django.db import models
# from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Rider(models.Model):
    username = models.CharField(max_length=200)
    cellphone = models.CharField(max_length=200)
    car_type = models.CharField(max_length=200)
    license_plate = models.CharField(max_length=200)
    rides_driven = models.TextField()#need to use this when upgrade to postgres --> ArrayField(models.CharField(max_length=20, blank=True),size=20)

    rides_passenger = models.TextField()#ArrayField(models.CharField(max_length=20, blank=True), size=20)
    rides_pending = models.TextField(default=",")
    rides_declined = models.TextField(default=",")

    def __str__(self):
        return self.username