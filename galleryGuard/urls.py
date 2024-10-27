from django.urls import include, path
from .views import index # Assurez-vous que toutes les vues sont importées
from django.contrib import admin


urlpatterns = [
    path('',include('Person.urls')),
    
    path('', index, name='home'),  # Route pour la page d'accueil
    path('admin/', admin.site.urls),  # Add this line   

   
]
