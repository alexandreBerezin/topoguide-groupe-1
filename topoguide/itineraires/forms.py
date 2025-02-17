from django import forms
from django.forms import ModelForm
from .models import Commentaire, Sortie

# formulaire pour ajouter ou modifier une sortie, il prend en compte tous les champs d'une sortie du modèle
# Sortie, sauf l'utilisateur (imposé puisque c'est l'utilisateur connecté) et l'itinéraire puisque la sortie
# s'ajoute pour l'itinéraire pour lequel on regarde les sorties
class SortieForm(ModelForm):
    class Meta:
        model = Sortie
        fields = ('date_sortie','duree_reelle','nombre_participants','experience_groupe','meteo','difficulte_ressentie','photo1','photo2','photo3')
        labels = {
            'date_sortie': 'Date de la sortie',
            'duree_reelle': 'Durée de la sortie',
            'nombre_participants': 'Nombre de participants',
            'experience_groupe': 'Experience du groupe',
            'meteo': 'Méteo lors de la sortie',
            'difficulte_ressentie': 'Difficulté ressentie',
            'photo1' : 'Photo n°1',
            'photo2' : 'Photo n°2',
            'photo3' : 'Photo n°3',
        }
        widgets = {
            'date_sortie': forms.DateInput(attrs={'type' : 'date','class':'form-control'}),
            'duree_reelle': forms.NumberInput(attrs={'class':'form-control'}),
            'nombre_participants': forms.NumberInput(attrs={'class':'form-control'}),
            'experience_groupe': forms.Select(attrs={'class':'form-control'}),
            'meteo': forms.Select(attrs={'class':'form-control'}),
            'difficulte_ressentie': forms.NumberInput(attrs={'class':'form-control'}),
            'photo1' : forms.FileInput(attrs={'class':'form-control'}),
            'photo2' : forms.FileInput(attrs={'class':'form-control'}),
            'photo3' : forms.FileInput(attrs={'class':'form-control'}),
        }

class CommentaireForm(ModelForm):
    class Meta:
        model = Commentaire
        fields = ('statut','texte')
        labels = {
            'statut': 'Commentaires',
            'texte' : '',
        }
        widgets = {
            'texte': forms.Textarea(attrs={'class':'form-control','rows':'3'}),
            
        }


