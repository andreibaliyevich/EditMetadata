from django import forms
from django.core import validators
from django.utils import timezone


class UploadImageGPSForm(forms.Form):
    image = forms.ImageField(
        validators=[
            validators.FileExtensionValidator(
                allowed_extensions=('jpg',)),
        ],
        error_messages={
            'invalid_extension': 'This file format is not supported.'},
    )

    date = forms.DateTimeField(initial=timezone.now)

    latitude_a = forms.DecimalField(label='Latitude angle')
    latitude_m = forms.DecimalField(label='Latitude minute')
    latitude_s = forms.DecimalField(label='Latitude second')

    LATITUDE_REF_CHOICES = [
        ('N', 'north latitude'),
        ('S', 'south latitude'),
    ]
    latitude_ref = forms.ChoiceField(
        label='Latitude ref',
        choices=LATITUDE_REF_CHOICES,
        initial='N',
    )

    longitude_a = forms.DecimalField(label='Longitude angle')
    longitude_m = forms.DecimalField(label='Longitude minute')
    longitude_s = forms.DecimalField(label='Longitude second')

    LONGITUDE_REF_CHOICES = [
        ('E', 'east longitude'),
        ('W', 'west longitude'),
    ]
    longitude_ref = forms.ChoiceField(
        label='Longitude ref',
        choices=LONGITUDE_REF_CHOICES,
        initial='E',
    )
