from django.contrib import admin

from .models import Itineraire, Sortie, Commentaire

# Register your models here.

admin.site.register(Itineraire) 
admin.site.register(Sortie)
admin.site.register(Commentaire)
