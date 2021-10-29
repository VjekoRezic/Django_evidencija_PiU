from django.db import models
from django.db.models.fields import CharField

class VrstaPrometa(models.Model):
    vrstaPrometa=CharField(max_length=50)
    
