from django.urls import path 
from .views import RadnoMjestoDeleteView, RadnoMjestoListView, RadnoMjestoUpdateView, RadnoMjestoCreateView
from . import views

urlpatterns = [

    path('', views.smjene , name='smjene'),
    path('dodaj/', views.dodajSmjenuUTroskove, name='smjena-dodaj-troskove' ),
    path('pregled/', views.pregledSmjena, name='smjene-pregled'),
    path('ukloni/', views.ukloniSmjenu, name='smjene-ukloni'),
    path('radnaMjesta/', RadnoMjestoListView.as_view(), name='smjene-lista' ),
    path('radnaMjesta/<int:pk>/update', RadnoMjestoUpdateView.as_view(), name='smjena-update'),
    path('radnoMjesto/create',RadnoMjestoCreateView.as_view(), name='smjena-create' ),
    path('radnoMjesto/<int:pk>/delete', RadnoMjestoDeleteView.as_view(),name='smjena-delete')
    
    
]