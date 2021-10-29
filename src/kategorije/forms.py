from django import forms
from .models import Kategorija

class KategorijaForm(forms.ModelForm):
    class Meta:
        model = Kategorija
        fields=['kategorija']
