from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render
from django.urls.base import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from ulazni_paketi.forms import PaketForm
from django.urls import reverse

from ulazni_paketi.models import UlazniPaket


class PaketListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model=UlazniPaket
    context_object_name="paketi"

    def test_func(self):
        
        if self.request.user.is_superuser:
            return True
        return False

class PaketUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model=UlazniPaket
    form_class=PaketForm

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        return form
    
    def form_valid(self, form):
        
        return super().form_valid(form)

    def test_func(self):
        
        if self.request.user.is_superuser:
            return True
        return False
    def get_success_url(self):
        return reverse('paket-list')

class PaketCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model=UlazniPaket
    form_class=PaketForm

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        return form
    
    def form_valid(self, form):
        
        return super().form_valid(form)

    def test_func(self):
        
        if self.request.user.is_superuser:
            return True
        return False
    def get_success_url(self):
        return reverse('paket-list')

class PaketDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model=UlazniPaket

    def get_success_url(self) :
        return reverse_lazy('paket-list')
    
    def test_func(self):
        
        if self.request.user.is_superuser:
            return True
        return False
