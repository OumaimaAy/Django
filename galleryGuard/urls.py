from django.urls import path
from .views import index # Assurez-vous que toutes les vues sont importées

urlpatterns = [
    path('', index, name='home'),  # Route pour la page d'accueil
   
]
