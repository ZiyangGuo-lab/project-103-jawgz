from django import template
from user_profile.models import Rider
from find.models import Posting
from datetime import datetime, timezone, timedelta
import os

register = template.Library()

@register.simple_tag
def get_user_image(value):
    user_matches = Rider.objects.filter(username=value)
    if (user_matches.exists()):
        user = user_matches[0]
        if (user.image):

            image_link = 'https://hoosriding.s3.amazonaws.com/profile_images/' + os.path.basename(user.image.file.name)
            return image_link
        else:
            return 'https://www.w3schools.com/howto/img_avatar2.png'
    else:
        return 'https://www.w3schools.com/howto/img_avatar2.png'


@register.simple_tag
def get_name(value):
    user_matches = Rider.objects.filter(username=value)
    if (user_matches.exists()):
        user = user_matches[0]
        if (user.name):
            return user.name
        else:
            return value
    else:
        return value


@register.simple_tag
def get_cellphone(value):
    user_matches = Rider.objects.filter(username=value)
    if (user_matches.exists()):
        user = user_matches[0]
        if (user.cellphone):
            return user.cellphone
        else:
            return 'No phone number provided.'
    else:
        return 'No phone number provided'


@register.simple_tag
def get_license_plate(value):
    user_matches = Rider.objects.filter(username=value)
    if (user_matches.exists()):
        user = user_matches[0]
        if (user.license_plate):
            return user.license_plate
        else:
            return 'No license plate provided.'
    else:
        return 'No license plate provided.'


@register.simple_tag
def get_car(value):
    user_matches = Rider.objects.filter(username=value)
    if (user_matches.exists()):
        user = user_matches[0]
        if (user.car_type):
            return user.car_type
        else:
            return 'No car information provided.'
    else:
        return 'No car information provided.'

@register.simple_tag
def get_rating(value):
    user_matches = Rider.objects.filter(username=value)
    if (user_matches.exists()):
        user = user_matches[0]
        if (user.rating):
            return user.rating
        else:
            return 'No car information provided.'
    else:
        return 'No car information provided.'

@register.simple_tag
def has_occurred(riding_date):
    return (datetime.now(timezone.utc) - timedelta(hours=5)) > riding_date

@register.simple_tag
def is_ratable(current_user, posting):
    posting = Posting.objects.filter(posting_id=posting)[0]
    ratable_list = posting.ratable_by.split(',')

    current_user = str(current_user)
    if current_user in ratable_list:
        return True
    else:
        return False

@register.simple_tag
def define(val):
    return val




