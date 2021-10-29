from django.db import models
from django.db.models.deletion import CASCADE
from kategorije.models import Kategorija

from ulazni_paketi.models import UlazniPaket

class Artikal(models.Model):
    artikal=models.CharField(max_length=50)
    stanje=models.DecimalField(decimal_places=3, max_digits=6)
    normativ=models.DecimalField(decimal_places=3, max_digits=4)
    cijena=models.DecimalField(decimal_places=2, max_digits=5)
    ulazniPaket=models.ForeignKey(UlazniPaket, on_delete=CASCADE)
    nabavnaCijena=models.DecimalField(decimal_places=2, max_digits=6)
    kategorija=models.ForeignKey(Kategorija,on_delete=CASCADE)
    uPonudi=models.BooleanField(default=True)

