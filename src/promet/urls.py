from django.urls import path 
from .views import PrometListView
from . import views

urlpatterns = [
    path('spremiRacun/', views.spremiRacun, name='promet-spremi-racun'),
    path('spremiSmjene/', views.spremiSmjene, name='promet-spremi-smjene'),
    path('spremiDonos/', views.spremiUlazniRacun, name='promet-spremi-donos'),
    path('pregledPrometa/', PrometListView.as_view(), name='promet_list')
   
    
]