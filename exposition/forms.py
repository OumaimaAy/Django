from django import forms
from .models import Exposition

class ExpositionForm(forms.ModelForm):
    class Meta:
        model = Exposition
        fields = ['nom', 'description', 'date_fabrication', 'nom_fabricant', 'mots_cles', 'image'] 