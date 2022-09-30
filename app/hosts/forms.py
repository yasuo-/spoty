from django import forms
from django.contrib.auth import get_user_model
# from betterforms.multiform import MultiModelForm

from .models import Host, Place, PlaceItem

User = get_user_model()


class HostModelForm(forms.ModelForm):
    class Meta:
        model = Host
        # fields = ("user",)
        # user = forms.HiddenInput()


class PlaceModelForm(forms.ModelForm):
    """
    Place Form
    """
    class Meta:
        model = Place
        fields = (
            "host",
            "title",
            "body",
            "prefecture",
            "city",
            "address",
            "address1",
            "phone",
            "time_frame",
        )
        host = forms.HiddenInput()
        title = forms.CharField(label="店舗名", max_length=200)
        body = forms.CharField(label="店舗 情報", max_length=200)
        postal_code = forms.CharField(label="郵便番号", max_length=10)
        address1 = forms.CharField(label="address1", max_length=200)


class PlaceItemModelForm(forms.ModelForm):

    class Meta:
        model = PlaceItem
        fields = ("place", "name", "price_per_time_frame",)
        place = forms.HiddenInput()
        name = forms.CharField(label="店舗名 貸出先名", max_length=200)
