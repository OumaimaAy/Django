import io
from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
import requests
from .models import Exposition
from .forms import ExpositionForm
import os
from django.conf import settings
from django.shortcuts import render


# from transformers import VisionEncoderDecoderModel, ViTImageProcessor, GPT2Tokenizer ,  GPT2LMHeadModel
from PIL import Image
import requests
# import torch

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


  
# import io
# import requests
# from PIL import Image
# from django.shortcuts import render

# MODEL_URL = "https://api-inference.huggingface.co/models/nlpconnect/vit-gpt2-image-captioning"
# TOKEN = "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"

# def generate_caption(image):
#     # Convert the image to bytes
#     image_byte_arr = io.BytesIO()
#     image.save(image_byte_arr, format='PNG')
#     image_bytes = image_byte_arr.getvalue()

#     # Prepare the headers for the request
#     headers = {
#         "Authorization": f"Bearer {TOKEN}",
#         "Content-Type": "application/octet-stream"
#     }

#     # Send the image to the Hugging Face API for caption generation
#     response = requests.post(MODEL_URL, headers=headers, data=image_bytes)
    
#     if response.status_code == 200:
#         caption = response.json().get("caption", "No caption generated.")
#     else:
#         caption = "Error: Unable to generate caption."

#     return caption

# def get_image_information(request, image_url):
#     caption = None
#     if request.method == 'POST':
#         # Open the image from the URL
#         image = Image.open(requests.get(image_url, stream=True).raw)

#         # Generate the image caption
#         caption = generate_caption(image)

#     # Render the result in your HTML template
#     return render(request, 'expositions/image_info.html', {'caption': caption, 'image_url': image_url})