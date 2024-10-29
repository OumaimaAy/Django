# memberships/forms.py
from django import forms
from .models import Reclamation
from .models import Response


class ReclamationForm(forms.ModelForm):
    class Meta:
        model = Reclamation
        fields = ['title', 'description', 'priority', 'category', 'attachment']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'priority': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'attachment': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
class ResponseForm(forms.ModelForm):
    class Meta:
        model = Response
        fields = ['content']  # The fields you want to include in the form
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Type your response here...'}),
        }