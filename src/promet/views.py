
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import CreateView , ListView, UpdateView,  DeleteView
from artikli.models import Artikal
from smjene.models import Smjena
from vrsta_prometa.models import VrstaPrometa
from .models import Promet
from helpers import helpers
import datetime

@login_required
def spremiRacun(request):
    try:
        if request.method!="POST":

            return HttpResponse("Bad request")
        
        elif helpers.racun=={}:
            return HttpResponse("<h1>Račun je prazan</h1>")

        else:
            prometBaza= Promet.objects.filter(datum=datetime.date.today(), smjena= None, vrstaPrometa=VrstaPrometa.objects.filter(vrstaPrometa="Dobit").first()).all()
            racun= helpers.racun
            for key, trazeniArtikal in racun.items():
                #provjera ima li na stanju potrebna količina , ako ima oduzimam kolicina+normativ od stanja
                artikal= Artikal.objects.filter(artikal=trazeniArtikal.artikal.artikal).first()
                if (artikal.stanje < (trazeniArtikal.kvantiteta * artikal.normativ)):
                    return HttpResponse("<h1>Nema dovoljno "+artikal.artikal+" na stanju </h1>")
                
                


                artikal.stanje= artikal.stanje - (trazeniArtikal.kvantiteta * artikal.normativ)
                artikal.save()

                x=prometBaza.filter(artikal=trazeniArtikal.artikal).first()
                if (x!=None):
                    x.ukupno= x.ukupno + (x.artikal.cijena * trazeniArtikal.kvantiteta)
                    x.kvantiteta=x.kvantiteta + trazeniArtikal.kvantiteta
                    x.save()
                else:
                    x=trazeniArtikal
                    x.save()
                
            helpers.racun.clear()
            
            
        return redirect('artikli')
    except Exception as e:
        return HttpResponse("<h1> Ne valja nešto "+ e + "</h1>")

@login_required
def spremiSmjene(request):
    try:
        if request.method!="POST":

            return HttpResponse("Bad request")
        
        elif helpers.smjene=={}:
            return HttpResponse("<h1>No data</h1>")

        else:
            prometBaza= Promet.objects.filter(datum=datetime.date.today(), smjena = not None, vrstaPrometa=VrstaPrometa.objects.filter(vrstaPrometa="Troškovi").first()).all()
            smj= helpers.smjene
            for key, trazenaSmj in smj.items():
                x=prometBaza.filter(smjena =trazenaSmj.smjena).first()
                if (x!=None):
                    x.ukupno= x.ukupno + (x.smjena.iznos * trazenaSmj.kvantiteta)
                    x.kvantiteta=x.kvantiteta + trazenaSmj.kvantiteta
                    x.save()
                else:
                    x=trazenaSmj
                    x.save()
            helpers.smjene.clear()
            
        return redirect('artikli')
                



    except Exception as e:
        return HttpResponse("<h1> Ne valja nešto "+ e + "</h1>")
   
@login_required
def spremiUlazniRacun(request):
    try:
        if request.method!="POST":

            return HttpResponse("Bad request")
        
        elif helpers.unos=={}:
            return HttpResponse("<h1>Račun je prazan</h1>")

        else:
            prometBaza= Promet.objects.filter(datum=datetime.date.today(), vrstaPrometa = VrstaPrometa.objects.filter(vrstaPrometa="Troškovi").first(), smjena = None).all()
            racun= helpers.unos
            for key, trazeniArtikal in racun.items():
                #stanje + broj artikala po ulaznom paketu * broj ulaznih paketa
                artikal= Artikal.objects.filter(artikal=trazeniArtikal.artikal.artikal).first()                
                artikal.stanje= artikal.stanje + (trazeniArtikal.kvantiteta * artikal.ulazniPaket.kvantiteta)
                artikal.save()

                x=prometBaza.filter(artikal=trazeniArtikal.artikal).first()
                if (x!=None):
                    x.ukupno= x.ukupno + (x.artikal.cijena * trazeniArtikal.kvantiteta)
                    x.kvantiteta=x.kvantiteta + trazeniArtikal.kvantiteta
                    x.save()
                else:
                    x=trazeniArtikal
                    x.save()
            helpers.unos.clear()
            
        return redirect('artikli')
    except Exception as e:
        return HttpResponse("<h1> Ne valja nešto "+ e + "</h1>")

class PrometListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model=Promet
    
    def test_func(self):
        
        if self.request.user.is_superuser:
            return True
        return False

    def get_context_data(self, **kwargs):
        today=datetime.date.today()
        
        dt=self.request.GET.get('datum')
        if dt!=None:
            format = '%Y-%m-%d'
            dt=datetime.datetime.strptime(dt, format)
        else:
            dt=today
        prometDana= Promet.objects.filter(datum=dt )
        data = super().get_context_data(**kwargs)
        data['prihodiLista']= prometDana.filter(vrstaPrometa = VrstaPrometa.objects.filter(vrstaPrometa="Dobit").first())
        data['donos']= prometDana.filter(smjena=None , vrstaPrometa = VrstaPrometa.objects.filter(vrstaPrometa="Troškovi").first())
        data['smjene']=prometDana.filter(artikal=None , vrstaPrometa = VrstaPrometa.objects.filter(vrstaPrometa="Troškovi").first())
        data['prihodi']=sum([item.ukupno for item in data["prihodiLista"]])
        data['troškovi']=sum([item.ukupno for item in data["donos"]])
        data['smjeneUkupno']=sum([item.ukupno for item in data["smjene"]])
        data['ukupno']=data["prihodi"]-data["troškovi"]-data["smjeneUkupno"]
        data["datum"]=dt    
    	

        return data
    