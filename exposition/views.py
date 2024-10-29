import io
import json
from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
import requests
from .models import Exposition
from .forms import ExpositionForm
import os
from django.conf import settings
from django.shortcuts import render


from transformers import VisionEncoderDecoderModel, ViTImageProcessor, GPT2Tokenizer ,  GPT2LMHeadModel
from PIL import Image
import requests
import torch
import google.generativeai as genai
import os

# Vue pour afficher la liste des expositions
def liste_expositions(request):
    expositions = Exposition.objects.all()
    return render(request, 'expositions/liste.html', {'expositions': expositions})

# Vue pour afficher les détails d'une exposition
def detail_exposition(request, pk):
    exposition = get_object_or_404(Exposition, pk=pk)
    return render(request, 'expositions/detail.html', {'exposition': exposition})

# Vue pour ajouter une nouvelle exposition
def ajouter_exposition(request):
    if request.method == "POST":
        form = ExpositionForm(request.POST, request.FILES)  # Ajoutez request.FILES
        if form.is_valid():
            form.save()
            messages.success(request, "L'exposition a été ajoutée avec succès.")
            return redirect('liste_expositions')  # Redirige vers la liste des expositions après l'ajout
    else:
        form = ExpositionForm()
    return render(request, 'expositions/formulaire.html', {'form': form})

# Vue pour modifier une exposition existante
def modifier_exposition(request, pk):
    exposition = get_object_or_404(Exposition, pk=pk)
    if request.method == "POST":
        form = ExpositionForm(request.POST, request.FILES, instance=exposition)  # Ajoutez request.FILES
        if form.is_valid():
            form.save()
            messages.success(request, "L'exposition a été modifiée avec succès.")
            return redirect('liste_expositions')
    else:
        form = ExpositionForm(instance=exposition)
    return render(request, 'expositions/formulaire.html', {'form': form})

# Vue pour supprimer une exposition
def supprimer_exposition(request, pk):
    exposition = get_object_or_404(Exposition, pk=pk)
    if request.method == "POST":
        exposition.delete()
        messages.success(request, "L'exposition a été supprimée avec succès.")
        return redirect('liste_expositions')
    return render(request, 'expositions/confirmer_suppression.html', {'exposition': exposition})

#ai 


  
import io
import requests
from PIL import Image
from django.shortcuts import render


MODEL_URL = "https://api-inference.huggingface.co/models/nlpconnect/vit-gpt2-image-captioning"
TOKEN = "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"

def generate_caption(image_path):
    # Ouvrir l'image locale
    with Image.open(image_path) as image:
        # Convertir l'image en bytes
        image_byte_arr = io.BytesIO()
        image.save(image_byte_arr, format='PNG')  # Sauvegarder au format PNG
        image_bytes = image_byte_arr.getvalue()

    # Préparer les headers pour la requête
    headers = {
        "Authorization": f"Bearer {TOKEN}",
        "Content-Type": "application/octet-stream"
    }

    # Envoyer l'image à l'API Hugging Face pour générer la description
    response = requests.post(MODEL_URL, headers=headers, data=image_bytes)
    
    # Vérifier la réponse
    if response.status_code == 200:
        # Extraire la légende de la réponse
        caption = response.json().get("generated_text", "No caption generated.")
    else:
        caption = "Error: Unable to generate caption."

    return caption

def get_image_information(request):
    if request.method == 'POST':
        # Récupérer le chemin de l'image locale depuis la requête POST
        image_path = request.POST.get('image_path')
        
        # Générer la légende pour l'image
        caption = generate_caption(image_path)

        # Afficher le résultat dans le template HTML
        return render(request, 'expositions/image_info.html', {'caption': caption, 'image_path': image_path})

    return render(request, 'expositions/image_info.html')

#AITEXT
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=GOOGLE_API_KEY)

#def ai_generate_description(request , nom):
   # model = genai.GenerativeModel('gemini-1.5-flash')
    #prompt = f"Generate a detailed description for an exposition in a musem  with the name  in 4 lines: {nom}"
    
    #response = model.generate_content(prompt)
    #return HttpResponse ( response.text)

genai.configure(api_key='AIzaSyBnBLiWwlkozcpLB1N0QgyXrcD3QdTuHW8')


def ai_generate_description(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            nom = data.get('nom', '')

            if not nom:
                return JsonResponse({'error': 'Nom manquant'}, status=400)

            print(f"Nom reçu: {nom}")  

            model = genai.GenerativeModel('gemini-1.5-flash')
            prompt = f"Generate a detailed description for an exposition in a museum with the name in 4 lines: {nom}"

            response = model.generate_content(prompt)
            return JsonResponse({'description': response.text})

        except Exception as e:
            print(f"Erreur: {str(e)}")  
            return JsonResponse({'error': 'Erreur interne du serveur'}, status=500)

    return JsonResponse({'error': 'Méthode non autorisée'}, status=405)
