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
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth.mixins import LoginRequiredMixin
# import json
# from Person.models import Person


# from django.core.files import File
# import io
# from PIL import Image  
import os

from venv import logger
from django.views.generic import ListView
from django.db.models import Q

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .models import Event
from .forms import EventForm
from django.shortcuts import render
from django.views.generic import DetailView
import google.generativeai as genai

from django.http import JsonResponse

genai.configure(api_key="AIzaSyDU0BkGkdcopb7pNGmOZIEL950XOHoClZM")


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
    
    
from django.http import JsonResponse
from google.generativeai import GenerativeModel  # Adjust based on your actual import

def suggestion_view(request):
    model = GenerativeModel('gemini-1.5-flash')  # Adjust the model as necessary
    user_input = request.GET.get('q', '').strip()
    print(f"User input: '{user_input}'")
    suggestions = []

    # Fetch events from the database
    events = Event.objects.all()  # Modify this query based on your requirements
    event_titles = [event.title for event in events]

    if user_input:
        try:
            # Create a string of existing event titles
            events_string = ", ".join(event_titles)

            # Define a prompt that includes the user input and existing events
            prompt = (f"Based on the user input '{user_input}', suggest related events or ideas "
                      f"from the following events: {events_string}.")

            # Attempt to generate content with the prompt
            response = model.generate_content(prompt)  # Call without 'content' keyword

            # Log the response from the API
            print("Response from API:", response)

            # Check the response structure
            if hasattr(response, 'text'):
                raw_text = response.text
                print("Raw response text:", raw_text)

                # Parse the response into suggestions
                suggestions = [suggestion.strip() for suggestion in raw_text.split('\n') if suggestion.strip()]

            else:
                print("No text attribute found in the response.")
        except Exception as e:
            print(f"Erreur d'API Google Generative AI : {e}")

    return JsonResponse({'suggestions': suggestions})









class EventListView(ListView):
    model = Event
    template_name = "event/event_list.html"  # Créez ce template
    context_object_name = 'events'  # Le nom de la variable dans le template
    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get("q")
        if query:
            queryset = queryset.filter(
                Q(title__icontains=query) | Q(description__icontains=query) | Q(category__icontains=query)
            )
        return queryset

class EventDetailView(LoginRequiredMixin, DetailView):
    model = Event
    template_name = "event/event_detail.html"  # Name of the template for displaying details
    context_object_name = "event"

    # Optional: Customize the login redirect URL
    login_url = reverse_lazy('register') 
    