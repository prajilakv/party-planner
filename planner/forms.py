from django.conf import settings

from django import forms
from .models import Guests, Finance, Buffet


class GuestForm(forms.ModelForm):
    class Meta:
        model = Guests
        fields = '__all__'


class FinanceForm(forms.ModelForm):
    class Meta:
        model = Finance
        fields = '__all__'


class BuffetForm(forms.ModelForm):
    class Meta:
        model = Buffet
        fields = '__all__'
        #exclude = ["user"]
