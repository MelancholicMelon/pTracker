from django import forms
from .models import ParkingLot


class ParkingLotForm(forms.ModelForm):
    class Meta:
        model = ParkingLot
        fields = ['name', 'latitude', 'longitude', 'picture']
