from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import CreateView , ListView, UpdateView,  DeleteView
from django.urls import reverse_lazy

from helpers import helpers
from smjene.forms import RadnoMjestoForma
from vrsta_prometa.models import VrstaPrometa
from promet.models import Promet
from smjene.models import Smjena

@login_required
def smjene(request):
    smjene=Smjena.objects.all()
    context= {
        "smjene": smjene
    }
    return render(request, 'smjene/smjene.html', context )
@login_required
def dodajSmjenuUTroskove(request):
    
    smjena= Smjena.objects.filter(id=request.GET.get('id')).first()
    troskovi= Promet(artikal=None, smjena=smjena, kvantiteta=1, ukupno=smjena.iznos, vrstaPrometa=VrstaPrometa.objects.filter(vrstaPrometa="Troškovi").first())
    
    if(smjena.radnoMjesto in helpers.smjene):
        helpers.smjene[smjena.radnoMjesto].kvantiteta+=1
        helpers.smjene[smjena.radnoMjesto].ukupno+=smjena.iznos
       
        


    
    else:
        helpers.smjene[smjena.radnoMjesto]=troskovi
        

    return HttpResponse( "Uspješno dodano",status=200 )
@login_required
def pregledSmjena(request):

    smjene=helpers.smjene
    if smjene=={}:
        return HttpResponse("<h1>This is empty!!</h1>")
    context= {"smjene":smjene}
    return render(request, 'smjene/pregled_smjena.html', context)
    
@login_required  
def ukloniSmjenu(request):
    smjene=helpers.smjene
    try:
        smj = request.GET.get('smjena')
        
        if (smj=="")or(smj==None):
            return HttpResponse( "Error, bad request",status=400 )
        elif(smjene[smj].kvantiteta==1):

            smjene.pop(smj)
            
            context= {
                "smjene":smjene,
                "message":"Uspješno uklonjeno",
                "status":200

            }
            return render(request, 'smjene/pregled_smjena.html', context)
        else:
            smjene[smj].kvantiteta=smjene[smj].kvantiteta-1
            smjene[smj].ukupno=smjene[smj].ukupno - smjene[smj].smjena.iznos
            context= {
                "racun":smjene,
                "message":"Uspješno uklonjeno",
                "status":200

            }
            return render(request, 'smjene/pregled_smjena.html', context)


            
    except Exception as e:
        return HttpResponse(str(e))


class RadnoMjestoListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Smjena
    context_object_name='radnaMjesta'


    def test_func(self):
        
        if self.request.user.is_superuser:
            return True
        return False

class RadnoMjestoUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model=Smjena
    form_class=RadnoMjestoForma

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        return form
    
    def form_valid(self, form):
        
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('smjene-lista')


    def test_func(self):
        
        if self.request.user.is_superuser:
            return True
        return False

class RadnoMjestoCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model=Smjena
    form_class=RadnoMjestoForma

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        return form
    
    def form_valid(self, form):
        
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('smjene-lista')


    def test_func(self):
        
        if self.request.user.is_superuser:
            return True
        return False

class RadnoMjestoDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model=Smjena

    def get_success_url(self):
        return reverse_lazy('smjene-lista')
    

    def test_func(self):
        
        if self.request.user.is_superuser:
            return True
        return False
    
    