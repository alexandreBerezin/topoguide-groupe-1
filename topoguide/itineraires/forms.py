from django import forms
from django.forms import ModelForm
from .models import Commentaire, Sortie

# formulaire pour ajouter ou modifier une sortie, il prend en compte tous les champs d'une sortie du modèle
# Sortie, sauf l'utilisateur (imposé puisque c'est l'utilisateur connecté) et l'itinéraire puisque la sortie
# s'ajoute pour l'itinéraire pour lequel on regarde les sorties
class SortieForm(ModelForm):
    class Meta:
        model = Sortie
        fields = ('date_sortie','duree_reelle','nombre_participants','experience_groupe','meteo','difficulte_ressentie','photo1')
        labels = {
            'date_sortie': 'Date de la sortie',
            'duree_reelle': 'Durée de la sortie',
            'nombre_participants': 'Nombre de participants',
            'experience_groupe': 'Experience du groupe',
            'meteo': 'Méteo lors de la sortie',
            'difficulte_ressentie': 'Difficulté ressentie',
        }
        widgets = {
            'date_sortie': forms.DateInput(attrs={'class':'form-control'}),
            'duree_reelle': forms.NumberInput(attrs={'class':'form-control'}),
            'nombre_participants': forms.NumberInput(attrs={'class':'form-control'}),
            'experience_groupe': forms.Select(attrs={'class':'form-control'}),
            'meteo': forms.Select(attrs={'class':'form-control'}),
            'difficulte_ressentie': forms.NumberInput(attrs={'class':'form-control'}),
        }

class CommentaireForm(ModelForm):
    class Meta:
        model = Commentaire
        fields = ('texte',)
        labels = {
            'texte': 'Commentaires : ',
        }


