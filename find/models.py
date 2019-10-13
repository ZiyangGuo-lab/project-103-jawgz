from django.db import models
from datetime import datetime, timedelta


def default_datetime():
    return datetime.now() + timedelta(days=1)

# ONE_TO_FIVE_RATING_CHOICES = (
#     (1, '1'),
#     (2, '2'),
#     (3, '3'),
#     (4, '4'),
#     (5, '5'),
# )

class Posting(models.Model):
    driver_name = models.CharField(max_length=200)
    vehicle_model = models.CharField(max_length=200)
    location_to = models.CharField(max_length=200)
    location_from = models.CharField(max_length=200)
    date = models.DateTimeField(default=default_datetime)
    price = models.CharField(max_length=200)
    # rating = models.IntegerField(choices=ONE_TO_FIVE_RATING_CHOICES)

    driver_id = models.CharField(max_length=200, default='0000000')
    uid = models.CharField(max_length=200, default='0000000')

    def __str__(self):
        return self.driver_name