from django import forms
from .models import Smjena

class RadnoMjestoForma(forms.ModelForm):
    class Meta:
        model = Smjena
        fields=['radnoMjesto', 'iznos']