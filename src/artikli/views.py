from django.shortcuts import render

from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required, user_passes_test
from artikli.forms import UpArtikal
from kategorije.models import Kategorija
from promet.models import Promet
from smjene.models import Smjena
from ulazni_paketi.models import UlazniPaket
from vrsta_prometa.models import VrstaPrometa
from .models import Artikal
from helpers import helpers
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

@login_required
def artikli(request):
    try:
        kategorija=request.GET.get('kategorija')
        if (kategorija=="")or(kategorija==None):
            kategorija="Topli Napitci"
    except Exception as e:
        print(str(e))
    
    
        


    artikli= Artikal.objects.filter(kategorija__kategorija= kategorija, stanje__gt = 0)
    kategorije=Kategorija.objects.all()

   
    context= {
        "artikli": artikli,
        "kategorije":kategorije
    }
    return render(request, 'artikli/artikli.html', context )
@login_required
def dodajNaRacun(request):
    
    
    artikal= Artikal.objects.filter(id=request.GET.get('id')).first()
    promet= Promet(artikal=artikal, smjena=None, kvantiteta=1, ukupno=artikal.cijena, vrstaPrometa=VrstaPrometa.objects.filter(vrstaPrometa="Dobit").first())
    
    if(artikal.artikal in helpers.racun):
        helpers.racun[artikal.artikal].kvantiteta+=1
        helpers.racun[artikal.artikal].ukupno+=artikal.cijena
        # print(helpers.racun[artikal.artikal].artikal.artikal)
        # print(helpers.racun[artikal.artikal].kvantiteta)
        # print(helpers.racun[artikal.artikal].ukupno)
        # print(helpers.racun[artikal.artikal].vrstaPrometa.vrstaPrometa)
        


    
    else:
        helpers.racun[artikal.artikal]=promet
        

    return HttpResponse( "Uspješno dodano",status=200 )

@login_required
def pregledRacuna(request):
    racun=helpers.racun
    if racun=={}:
        return HttpResponse("<h1>Nema ništa na računu!!</h1>")
    context= {"racun":racun}
    return render(request, 'artikli/pregled_racuna.html', context)

@login_required
def ukloniSRacuna(request):
    racun=helpers.racun
    try:
        artikal = request.GET.get('artikal')
        print(request)
        if (artikal=="")or(artikal==None):
            return HttpResponse( "Error, bad request",status=400 )
        elif(racun[artikal].kvantiteta==1):

            racun.pop(artikal)
            
            context= {
                "racun":racun,
                "message":"Uspješno uklonjeno",
                "status":200

            }
            return render(request, 'artikli/pregled_racuna.html', context)
        else:
            racun[artikal].kvantiteta=racun[artikal].kvantiteta-1
            racun[artikal].ukupno=racun[artikal].ukupno - racun[artikal].artikal.cijena
            context= {
                "racun":racun,
                "message":"Uspješno uklonjeno",
                "status":200

            }
            return render(request, 'artikli/pregled_racuna.html', context)


            
    except Exception as e:
        return HttpResponse(str(e))

@login_required
def donos(request):

    try:
        kategorija=request.GET.get('kategorija')
        if (kategorija=="")or(kategorija==None):
            kategorija="Topli Napitci"
    except Exception as e:
        print(str(e))

    artikli= Artikal.objects.filter(kategorija__kategorija= kategorija, stanje__gt = 0)
    kategorije=Kategorija.objects.all()

   
    context= {
        "artikli": artikli,
        "kategorije":kategorije
    }
    


    return render(request, 'artikli/donos.html', context)
@login_required
def dodajNaUlazniRacun(request):
    
    
    artikal= Artikal.objects.filter(id=request.GET.get('id')).first()
    promet= Promet(artikal=artikal, smjena=None, kvantiteta=1, ukupno=artikal.nabavnaCijena, vrstaPrometa=VrstaPrometa.objects.filter(vrstaPrometa="Troškovi").first())
    
    if(artikal.artikal in helpers.unos):
        helpers.unos[artikal.artikal].kvantiteta+=1
        helpers.unos[artikal.artikal].ukupno+=artikal.nabavnaCijena

    
    else:
        helpers.unos[artikal.artikal]=promet

    
        

    return HttpResponse( "Uspješno dodano",status=200 )
@login_required
def pregledUlaznogRacuna(request):
    racun=helpers.unos
    if racun=={}:
        return HttpResponse("<h1>Nema ništa na računu!!</h1>")
    context= {"racun":racun}
    return render(request, 'artikli/pregled_ulaznog_racuna.html', context)

@login_required
def ukloniDonos(request):
    racun=helpers.unos
    try:
        artikal = request.GET.get('artikal')
        print(request)
        if (artikal=="")or(artikal==None):
            return HttpResponse( "Error, bad request",status=400 )
        elif(racun[artikal].kvantiteta==1):

            racun.pop(artikal)
            
            context= {
                "racun":racun,
                "message":"Uspješno uklonjeno",
                "status":200

            }
            return render(request, 'artikli/pregled_ulaznog_racuna.html', context)
        else:
            racun[artikal].kvantiteta=racun[artikal].kvantiteta-1
            racun[artikal].ukupno=racun[artikal].ukupno - racun[artikal].artikal.nabavnaCijena
            context= {
                "racun":racun,
                "message":"Uspješno uklonjeno",
                "status":200

            }
            return render(request, 'artikli/pregled_ulaznog_racuna.html', context)

    except Exception as e:
        return HttpResponse(str(e))


class ArtikalUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model=Artikal
    form_class=UpArtikal

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['ulazniPaket'].choices = [(item.id, item.paket) for item in UlazniPaket.objects.all()]
        form.fields['kategorija'].choices = [(item.id, item.kategorija) for item in Kategorija.objects.all()]
        return form

    def form_valid(self, form):
        
        return super().form_valid(form)
    
    def test_func(self):
        
        if self.request.user.is_superuser:
            return True
        return False
    
    def get_success_url(self):
        return reverse('artikli')


class ArtikalCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):

    model=Artikal
    form_class=UpArtikal

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['ulazniPaket'].choices = [(item.id, item.paket) for item in UlazniPaket.objects.all()]
        form.fields['kategorija'].choices = [(item.id, item.kategorija) for item in Kategorija.objects.all()]
        return form

    def form_valid(self, form):
        
        return super().form_valid(form)

    def test_func(self):
        
        if self.request.user.is_superuser:
            return True
        return False
    
    def get_success_url(self):
        return reverse('artikli')

class ArtikalDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model=Artikal
    def test_func(self):
        
        if self.request.user.is_superuser:
            return True
        return False

    def get_success_url(self):
        return reverse_lazy('artikli')

  



        
