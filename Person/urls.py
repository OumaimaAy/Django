from django.urls import path
from .views import register # Assurez-vous que toutes les vues sont importées
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from .views import *
from .views import register # Assurez-vous que toutes les vues sont importées


urlpatterns = [
    path('register/', register, name="register"),
    path('logout/', LogoutView.as_view() , name="logout"),
    path('login/', login_user, name="login"),
    path('generate/', ai_generate_description, name='generate'),  # Ajoute cette ligne



   
]
