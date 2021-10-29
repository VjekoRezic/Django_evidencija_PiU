from django.urls import path 
from .views import PaketListView, PaketUpdateView, PaketCreateView, PaketDeleteView


urlpatterns = [

    path('list/', PaketListView.as_view(), name='paket-list'),
    path('<int:pk>/update/', PaketUpdateView.as_view(), name='paket-update'),
    path('create/', PaketCreateView.as_view(), name='paket-create'),
    path('<int:pk>/delete/', PaketDeleteView.as_view(), name='paket-delete')

    
]