print("Loading views.py")

# from django.shortcuts import render,redirect

# from .models import Event
# from django.views.generic import *

# from django.http import HttpResponse,JsonResponse
# # Create your views here.
# from .forms import EventForm

# from django.urls import reverse_lazy
# import google.generativeai as genai
# import requests
# import os
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth.mixins import LoginRequiredMixin
# import json
# from Person.models import Person


# from django.core.files import File
# import io
# from PIL import Image  

from venv import logger
from django.views.generic import ListView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .models import Event
from .forms import EventForm
from django.shortcuts import render
import logging


class AddEventView(LoginRequiredMixin, CreateView):
    model = Event
    template_name = "event/add.html"
    form_class = EventForm
    success_url = reverse_lazy("eventList")  # Change to your desired success URL

    def form_valid(self, form):
        form.instance.organisateur = self.request.user  # Assign the current user
        return super().form_valid(form)

    def form_invalid(self, form):
        print("Form is invalid:", form.errors)  # Print errors to the console
        return super().form_invalid(form)


def landing_page(request):
    events = Event.objects.all()  # Récupère tous les événements

    return render(request, 'index.html', {'events': events})
    


class EventListView(ListView):
    model = Event
    template_name = "event/event_list.html"  # Créez ce template
    context_object_name = 'events'  # Le nom de la variable dans le template

   
   