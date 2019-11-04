from django import forms

class ProfileForm(forms.Form):
    cellphone = forms.IntegerField()
    car_type = forms.CharField()
    license_plate = forms.CharField()
