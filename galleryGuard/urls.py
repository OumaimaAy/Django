from django.urls import include, path
from .views import index # Assurez-vous que toutes les vues sont importées
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('',include('Person.urls')),
    
    path('', index, name='home'),  # Route pour la page d'accueil
    path('admin/', admin.site.urls),  # Add this line   
    path('event/' , include('Event.urls') ),

   
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)