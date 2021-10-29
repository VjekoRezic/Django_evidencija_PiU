from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import DecimalField
from django.db.models.fields.related import ForeignKey

from artikli.models import Artikal
from smjene.models import Smjena
from vrsta_prometa.models import VrstaPrometa

class Promet(models.Model):
    datum=models.DateField(auto_now_add=True)
    artikal=models.ForeignKey(Artikal, on_delete=CASCADE, null=True)
    smjena=models.ForeignKey(Smjena, on_delete=CASCADE, null=True)
    kvantiteta=models.IntegerField()
    ukupno=models.DecimalField(decimal_places=2, max_digits=7)
    vrstaPrometa=ForeignKey(VrstaPrometa, on_delete=CASCADE)

