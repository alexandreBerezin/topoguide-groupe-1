from django.urls import path

from . import views

urlpatterns = [
    path('', views.itineraires, name='itineraires'),
    path('sorties/<int:itineraire_id>/', views.sorties, name='sorties'),
    path('sorties/<int:itineraire_id>/sortie/<int:sortie_id>/', views.details, name='details'),
    path('sorties/<int:itineraire_id>/nouvelle_sortie/', views.nouvelle_sortie, name='nouvelle_sortie'),
    path('sorties/<int:itineraire_id>/modif_sortie/<int:sortie_id>', views.modif_sortie, name='modif_sortie'),
    path('recherche/',views.recherche,name='recherche')
]