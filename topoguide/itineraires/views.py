from django.template import loader
from django.http import Http404, HttpResponse
from django.shortcuts import render

from .models import Itineraire, Sortie

# Create your views here.

def itineraires(request):
    template = loader.get_template('itineraires/itineraires.html')
    if request.method == 'GET': # If the form is submitted
        search = request.GET.get('search', None)
        itineraire_list = Itineraire.objects.order_by('titre')[:]
        context = {
            'itineraire_list': itineraire_list,
            'search' : search,
        }
    else:
        itineraire_list = Itineraire.objects.order_by('titre')[:]
        context = {
            'itineraire_list': itineraire_list,
        }
    return HttpResponse(template.render(context, request))

def sorties(request, itineraire_id):
    try:
        itineraire= Itineraire.objects.get(pk=itineraire_id)
        sorties_list = Sortie.objects.filter(itineraire=itineraire).all()
    except Itineraire.DoesNotExist:
        raise Http404("L'intinéraire n'existe pas")
    return render(request, 'itineraires/sorties.html', {'itineraire': itineraire, 'sorties_list': sorties_list})
