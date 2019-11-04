# from django import forms
#
# class ProfileForm(forms.Form):
#     cellphone = forms.IntegerField()
#     car_type = forms.CharField()
#     license_plate = forms.CharField()


# forms
from django import forms
from user_profile.models import *


class update_profile_form(forms.ModelForm):
    class Meta:
        model = Rider
        fields = ("cellphone", "car_type", "license_plate")

    def __init__(self, *args, **kwargs):
        super(update_profile_form, self).__init__(*args, **kwargs)
