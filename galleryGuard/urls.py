from asyncio import events
from django.urls import include, path
from .views import blog_home, contact, gallery, index, ticket , events
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
      path('admin/', admin.site.urls),
    path('', index, name='home'),  # Route pour la page d'accueil
    path('about', index, name='about'),  # Route pour la page d'accueil
   path('gallery/', gallery, name='gallery'),
      path('/gallery/events/', events, name='events'),  # Ensure 'events' is used correctly
    path('/gallery/ticket/', ticket, name='ticket'),
    path('blog/',blog_home, name='blog_home'),
    path('contact/', contact, name='contact'),
    path('exposition/' , include('exposition.urls') )
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
