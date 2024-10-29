# memberships/urls.py
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


from .views import (
    ReclamationListView, ReclamationDetailView,
    ReclamationCreateView, ReclamationUpdateView, ReclamationDeleteView,ResponseDeleteView  
)

urlpatterns = [
    path('reclamations/', ReclamationListView.as_view(), name='reclamation-list'),  
    path('reclamations/<int:pk>/', ReclamationDetailView.as_view(), name='reclamation-detail'),
    path('reclamations/create/', ReclamationCreateView.as_view(), name='reclamation-create'),
    path('reclamations/<int:pk>/update/', ReclamationUpdateView.as_view(), name='reclamation-update'),
    path('reclamations/<int:pk>/delete/', ReclamationDeleteView.as_view(), name='reclamation-delete'),
    path('reclamations/<int:pk>/add-response/', views.add_response, name='response-add'),
     path('responses/<int:pk>/delete/', ResponseDeleteView.as_view(), name='response-delete'),  # Class-based


]
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)