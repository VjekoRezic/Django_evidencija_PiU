from django.urls import path 
from .views import KategorijaCreateView, KategorijaListView, KategorijaUpdateView, KategorijeDeleteView
from . import views

urlpatterns = [

    path('create/', KategorijaCreateView.as_view() , name='kategorije-create'),
    path('list/', KategorijaListView.as_view(), name='kategorije-list'),
    path('<int:pk>/update', KategorijaUpdateView.as_view(), name='kategorija-update'),
    path('<int:pk>/delete', KategorijeDeleteView.as_view(), name='kategorija-delete')

    



    
]