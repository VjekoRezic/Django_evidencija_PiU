from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render
from django.views.generic import CreateView , ListView, UpdateView
from django.views.generic.edit import DeleteView
from kategorije.forms import KategorijaForm
from django.urls import reverse, reverse_lazy

from kategorije.models import Kategorija

class KategorijaCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model=Kategorija
    form_class=KategorijaForm

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
        return reverse('kategorije-list')

class KategorijaListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model=Kategorija
    context_object_name="kategorije"

    def test_func(self):
        
        if self.request.user.is_superuser:
            return True
        return False

class KategorijaUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model=Kategorija
    form_class=KategorijaForm

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
        return reverse('kategorije-list')
    
class KategorijeDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model=Kategorija

    def get_success_url(self):
        return reverse_lazy('kategorije-list')
    

    def test_func(self):
        
        if self.request.user.is_superuser:
            return True
        return False
