from django.contrib import admin
from .models import Exposition

@admin.register(Exposition)
class ExpositionAdmin(admin.ModelAdmin):
    list_display = ('nom', 'date_fabrication', 'nom_fabricant', 'image')  
    search_fields = ('nom', 'description', 'nom_fabricant')  
    list_filter = ('date_fabrication',)  
    ordering = ('-date_fabrication',)  
    list_per_page = 10  

    # Personnalisation du formulaire d'ajout/modification
    fieldsets = (
        (None, {
            'fields': ('nom', 'description', 'nom_fabricant', 'date_fabrication', 'image')
        }),
    )

    def save_model(self, request, obj, form, change):
        if not obj.nom:
            raise ValueError("Le nom de l'exposition ne peut pas être vide.")
        super().save_model(request, obj, form, change)

    def delete_model(self, request, obj):
        obj.delete()
