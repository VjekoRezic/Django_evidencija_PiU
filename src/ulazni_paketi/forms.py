from django import forms
from .models import UlazniPaket

class PaketForm(forms.ModelForm):
    class Meta:
        model = UlazniPaket
        fields=['paket', 'kvantiteta']