from django.forms import ModelForm, TextInput, Textarea, Select
from .models import Event
from django import forms

class DateInput(forms.DateInput):
    input_type = 'date'

    

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'image', 'category', 'evt_date']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control bg-light text-dark'}),
            'description': forms.Textarea(attrs={'class': 'form-control bg-light text-dark'}),
            'image': forms.FileInput(attrs={'class': 'form-control bg-light text-dark'}),
            'category': forms.Select(attrs={'class': 'form-select bg-light text-dark'}),
            'evt_date': forms.DateInput(attrs={'class': 'form-control bg-light text-dark', 'type': 'date'}),
        }
