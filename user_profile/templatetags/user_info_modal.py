from django import template
from user_profile.models import Rider
from find.models import Posting
import os

register = template.Library()

@register.simple_tag
def get_user_image(value):
    print('id: ', value)
    user_matches = Rider.objects.filter(username=value)
    if (user_matches.exists()):
        user = user_matches[0]
        if (user.image):

            image_link = 'https://hoosriding.s3.amazonaws.com/profile_images/' + os.path.basename(user.image.file.name)
            return image_link
        else:
            return 'https://www.w3schools.com/howto/img_avatar2.png'
    else:
        print('no user')
        return 'https://www.w3schools.com/howto/img_avatar2.png'


@register.simple_tag
def get_name(value):
    print('in get_name', value)
    user_matches = Rider.objects.filter(username=value)
    if (user_matches.exists()):
        user = user_matches[0]
        if (user.name):
            return user.name
        else:
            return value
    else:
        print('no user')
        return value


@register.simple_tag
def get_cellphone(value):
    print('id: ', value)
    user_matches = Rider.objects.filter(username=value)
    if (user_matches.exists()):
        user = user_matches[0]
        if (user.cellphone):
            return user.cellphone
        else:
            return 'No phone number provided.'
    else:
        print('no user')
        return 'No phone number provided'


@register.simple_tag
def get_license_plate(value):
    print('id: ', value)
    user_matches = Rider.objects.filter(username=value)
    if (user_matches.exists()):
        user = user_matches[0]
        if (user.license_plate):
            return user.license_plate
        else:
            return 'No license plate provided.'
    else:
        print('no user')
        return 'No license plate provided.'


@register.simple_tag
def get_car(value):
    print('id: ', value)
    user_matches = Rider.objects.filter(username=value)
    if (user_matches.exists()):
        user = user_matches[0]
        if (user.car_type):
            return user.car_type
        else:
            return 'No car information provided.'
    else:
        print('no user')
        return 'No car information provided.'

@register.simple_tag
def get_rating(value):
    print('id: ', value)
    user_matches = Rider.objects.filter(username=value)
    if (user_matches.exists()):
        user = user_matches[0]
        if (user.rating):
            # print("ratings list",user.ratings_list)
            # print("rating", user.rating)
            return user.rating
        else:
            return 'No car information provided.'
    else:
        print('no user')
        return 'No car information provided.'

@register.simple_tag
def has_occurred(value):
    # posting = Posting.objects.filter(posting_id=value)
    return True

@register.simple_tag
def is_ratable(current_user, posting):
    posting = Posting.objects.filter(posting_id=posting)[0]
    print(posting)
    ratable_list = posting.ratable_by.split(',')
    print('ratablelist', ratable_list)

    current_user = str(current_user)
    if current_user in ratable_list:
        return True
    else:
        return False






