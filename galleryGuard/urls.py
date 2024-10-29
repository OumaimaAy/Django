from django.urls import path
from .views import index 
from django.contrib import admin
from django.urls import path, include # Assurez-vous que toutes les vues sont importées
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', index, name='home'),  # Route pour la page d'accueil
    path('admin/', admin.site.urls),
  path('memberships/', include('memberships.urls')), 
          path('accounts/', include('django.contrib.auth.urls')), 
path('reclamations/', include('reclamation.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)