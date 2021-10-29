from django import forms
from .models import Artikal

class UpArtikal(forms.ModelForm):
    
    class Meta:
        model = Artikal
        fields=['artikal','stanje','normativ','cijena','ulazniPaket', 'nabavnaCijena', 'kategorija']
