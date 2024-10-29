from django.urls import path
from . import views

from .views import membership_list, membership_create, membership_update, membership_delete

urlpatterns = [
    path('', membership_list, name='membership_list'),
    path('create/', membership_create, name='membership_create'),
    path('update/<int:pk>/', membership_update, name='membership_update'),
    path('delete/<int:pk>/', membership_delete, name='membership_delete'),
]
