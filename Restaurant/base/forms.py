from django import forms
from .models import Reservation

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['user', 'table', 'reserv_date']
        widgets = {
            'reserv_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
