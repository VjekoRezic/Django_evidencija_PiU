from django.urls import path 
from .views import ArtikalUpdateView, ArtikalCreateView, ArtikalDeleteView
from . import views

urlpatterns = [

    path('', views.artikli , name='artikli'),
    path('dodajNaRacun/', views.dodajNaRacun ,  name='artikli-dodaj-na-racun'),
    path('racun/', views.pregledRacuna, name='artikli-pregled-racuna'),
    path('ukloni/', views.ukloniSRacuna, name='artikli-ukloni-s-racuna'),
    path('donos/',views.donos, name='artikli-donos'),
    path('dodajDonos/', views.dodajNaUlazniRacun, name='artikli-dodaj-donos'),
    path('donosPregled/', views.pregledUlaznogRacuna, name='artikli-pregled-ulaznog-racuna'),
    path('donosUkloni/', views.ukloniDonos, name='artikli-ukloni-donos'),
    path('<int:pk>/update/', ArtikalUpdateView.as_view(), name='artikli-update'),
    path('create/', ArtikalCreateView.as_view(), name='artikli-create'),
    path('<int:pk>/delete/', ArtikalDeleteView.as_view(), name='artikli-delete')



    
]