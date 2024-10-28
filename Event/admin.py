from django.contrib import admin
from .models import Event

class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'evt_date', 'state', 'nbr_participants')  # Changer les champs à afficher
    search_fields = ('title', 'description')  # Champs recherchables
    list_filter = ('category', 'state')  # Filtres dans l'admin

admin.site.register(Event, EventAdmin)
