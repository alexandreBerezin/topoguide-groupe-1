from django.conf import settings
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Itineraire(models.Model):
    """ Modèle qui permet de générer les différents champs d'informations pour un itinéaire
    dans la base de données et d'y accéder à partir des différents champs explicités ci-dessous
    """
    titre = models.CharField(max_length=200)
    point_depart = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    altitude_depart = models.IntegerField()
    altitude_min = models.IntegerField()
    altitude_max = models.IntegerField()
    denivele_neg = models.IntegerField()
    denivele_pos = models.IntegerField()
    duree_estimee = models.IntegerField()
    difficulte_estimee = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    def __str__(self):
        """ Permet de renvoyer avec la fonction string, le titre correctement pour visualiser """
        return self.titre

class Sortie(models.Model):
    """ Modèle qui permet de générer les différents champs d'informations pour une sortie
    dans la base de données et d'y accéder à partir des différents champs explicités ci-dessous
    """
    utilisateur = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    itineraire = models.ForeignKey(Itineraire, on_delete=models.CASCADE)
    date_sortie = models.DateField()
    duree_reelle = models.IntegerField()
    nombre_participants = models.IntegerField()
    EXPERIENCE_CHOIX = [
    ('TD', 'Tous débutants'),
    ('TE', 'Tous expérimentés'),
    ('MI', 'Mixte'),]
    experience_groupe = models.CharField(
        max_length=2,
        choices=EXPERIENCE_CHOIX,
        default='TD',
    )
    METEO_CHOIX = [
    ('BO', 'Bonne'),
    ('MO', 'Moyenne'),
    ('MA', 'Mauvaise'),]
    meteo = models.CharField(
        max_length=2,
        choices=METEO_CHOIX,
        default='MO',
    )
    difficulte_ressentie = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    
    '''Paramètres pour EXtension 1'''
    photo1 = models.ImageField(upload_to='photo/',default='default.jpg')
     
    
    
    def __str__(self):
        """ Permet de renvoyer avec la fonction string, le nom d'utilisateur correctement pour visualiser """
        return self.utilisateur.username