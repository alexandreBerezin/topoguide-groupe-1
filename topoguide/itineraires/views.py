from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required

from .forms import SortieForm
from .models import Itineraire, Sortie

# Create your views here.

# Vue accessible pour les utilisateurs connectés ou non de la même manière
def itineraires(request):
    """ Une fonction qui permet avec une requête de l'utilisateur d'obtenir la liste 
    des itinéraires disponibles avec leurs différents champs dans la base de données
    Il y a également une fonction de recherche qui permet à l'utilisateur de chercher parmi 
    les itinéraires existants

    Args:
        request : GET de l'utilisateur

    Returns:
        render(): réponse Http associant la fonction, le template associé (itineraire.html) et le contexte
        
    """
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
    return render(request, 'itineraires/itineraires.html', context)


# Vue accessible pour les utilisateurs connectés ou non de la même manière
def sorties(request, itineraire_id):
    """ Une fonction qui permet à partir de la requête utilisateur d'obtenir les sorties associées à un
    itinéraire. 

    Args:
        request : requête de l'utilisateur GET
        itineraire_id (int): id de l'itinéraire choisi par l'utilisateur pour en visualiser les sorties

    Raises:
        Http404: erreur 404 Http si l'itinéraire n'existe pas dans la base de données

    Returns:
        render(): réponse Http associant la fonction, le template associé (sorties.html) et le contexte
    """
    try:
        itineraire= Itineraire.objects.get(pk=itineraire_id)
        sorties_list = Sortie.objects.filter(itineraire=itineraire).all()
    except Itineraire.DoesNotExist:
        raise Http404("L'itinéraire n'existe pas")
    return render(request, 'itineraires/sorties.html', {'itineraire': itineraire, 'sorties_list': sorties_list})

# Vue accessible pour les utilisateurs connectés ou non avec des options d'ajout et de modification 
# seulement pour les utilisateurs connectés

def details(request, sortie_id, itineraire_id):
    """ Une fonction qui permet à partir de la requête utilisateur d'obtenir les détails d'une sortie
    en particulier à partir des informations de la base de données

    Args:
        request (): requête de l'utilisateur GET
        sortie_id (int): id de la sortie que l'on regarde en détails
        itineraire_id (int): id de l'itinéraire pour lequel on regarde les détails d'une sortie

    Raises:
        Http404: erreur 404 Http lorsque la sortie n'existe pas dans la base de données.

    Returns:
        render(): réponse Http associant la fonction, le template associé (details.html) et le contexte
    """
    try:
        sortie_detail = Sortie.objects.get(pk=sortie_id)
    except Sortie.DoesNotExist:
        raise Http404("La sortie n'existe pas")
    return render(request, 'itineraires/details.html', {'sortie_detail' : sortie_detail, 'itineraire_id' : itineraire_id})

# vue accessible seulement pour un utilisateur qui possède un compte et est authentifié 
@login_required
def nouvelle_sortie(request, itineraire_id):
    """ Une fonction qui permet de vérifier la validité du formulaire d'ajout d'une sortie en incluant
    ici l'utilisateur connecté et l'itinéraire pour laquelle la sortie est ajoutée (en fonction de la
    page dans laquelle se trouve l'utilisateur)

    Args:
        request (): requête de l'utilisateur GET ou POST
        itineraire_id (int): id de l'itinéraire associé à la nouvelle sortie

    Returns:
        render(): réponse Http associant la fonction, le template associé (nouvelle_sortie.html) et le contexte
    """
    
    submitted = False
    if request.method == 'POST':
        form = SortieForm(request.POST)
        if form.is_valid :
            form = form.save(commit=False)
            form.utilisateur = request.user
            form.itineraire = Itineraire.objects.get(pk=itineraire_id)
            form.save()
            submitted = True
    else : 
        form = SortieForm
        if submitted in request.GET:
            submitted = True
    return render(request, 'itineraires/nouvelle_sortie.html', {'form' : form, 'itineraire_id' : itineraire_id, 'submitted' : submitted})

# vue accessible seulement pour un utilisateur qui possède un compte et est authentifié 
@login_required
def modif_sortie(request, itineraire_id, sortie_id):
    """ Une fonction qui permet de vérifier la validité du formulaire pour la modification d'une sortie
    à partir de la requête utilisateur pour l'utilisateur qui a ajouté la sortie et lorsqu'il est connecté (vérifié 
    dans le template)

    Args:
        request (): _description_
        itineraire_id (int): id de l'itinéraire associé à la sortie à modifier
        sortie_id (int): id de la sortie à modifier

    Returns:
        render(): réponse Http associant la fonction, le template associé (nouvelle_sortie.html) et le contexte
    """
    submitted = False
    sortie = get_object_or_404(Sortie, id=sortie_id)
    if request.method == 'POST':
        form = SortieForm(request.POST or None, request.FILES or None, instance=sortie)
        if form.is_valid :
            form = form.save(commit=False)
            form.utilisateur = request.user
            form.itineraire = Itineraire.objects.get(pk=itineraire_id)
            form.save()
            submitted=True
        else:
            print("FORM NON VALIDE")
    else : 
        form = SortieForm(request.POST or None, instance=sortie)
    return render(request, 'itineraires/nouvelle_sortie.html', {'form' : form, 'itineraire_id' : itineraire_id, 'sortie_id' : sortie_id, 'submitted' : submitted})