from django.urls import path

from galleryGuard import settings
from . import views

urlpatterns = [
    path('exposition/', views.liste_expositions, name='liste_expositions'),
    path('<int:pk>/', views.detail_exposition, name='detail_exposition'),
    path('ajouter/', views.ajouter_exposition, name='ajouter_exposition'),
    path('<int:pk>/modifier/', views.modifier_exposition, name='modifier_exposition'),
    path('<int:pk>/supprimer/', views.supprimer_exposition, name='supprimer_exposition'),
    path('get-image-information/<path:image_url>/', views.get_image_information, name='get_image_information'),
    path('generate/<str:nom>' , views.ai_generate_description , name="generate"),
     path('generate-description/', views.ai_generate_description, name='generate_description'),
]

