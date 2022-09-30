from django import forms
from django.contrib.auth import get_user_model
# from betterforms.multiform import MultiModelForm

from .models import BookingCheckIn, BookingCheckOut

User = get_user_model()


class BookingCheckInModelForm(forms.ModelForm):
    class Meta:
        model = BookingCheckIn
        fields = ("booking",)
        booking = forms.HiddenInput()


class BookingCheckOutModelForm(forms.ModelForm):
    class Meta:
        model = BookingCheckOut
        fields = ("booking",)
        booking = forms.HiddenInput()
