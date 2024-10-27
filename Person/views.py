import google.generativeai as genai
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate
from .forms import UserRegisterForm
from django.shortcuts import render
from django.core.exceptions import ValidationError


# Configuration de l'API Google Gemini
genai.configure(api_key="AIzaSyDU0BkGkdcopb7pNGmOZIEL950XOHoClZM")



def ai_generate_description(request):
    model = genai.GenerativeModel('gemini-1.5-flash')
    prompt = "Generate a detailed description for an event with the title in 4 lines: Real Madrid"
    
    try:
        response = model.generate_content(prompt)
        generated_text = response.text if hasattr(response, 'text') else "Aucune réponse générée."
    except Exception as e:
        generated_text = f"Erreur lors de la génération : {e}"

    # Rendre un template avec le texte généré
    return render(request, 'auth/test_api.html', {'generated_text': generated_text})


def register(request):
    if request.user.is_authenticated:
        return redirect("home")
    
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Vous êtes maintenant inscrit !")
            return redirect("home")
        else:
            # Boucle à travers les erreurs de validation
            for field, errors in form.errors.items():
                for error in errors:
                    # Utilise Google Gemini pour générer un message d'erreur personnalisé
                    prompt_text = f"Générer un conseille tres court pour le champ '{field}' avec le message d'erreur suivant : '{error}'"
                    try:
                        response = genai.GenerativeModel('gemini-1.5-flash').generate_content(prompt_text)
                        error_message = response.text if hasattr(response, 'text') else "Erreur de validation."
                    except Exception as e:
                        error_message = "Erreur lors de la génération d'un message d'erreur."
                        print(f"Erreur avec Google Gemini : {e}")

                    # Afficher le message d'erreur sous le champ correspondant
                    messages.error(request, error_message)

    else:
        form = UserRegisterForm()
        
    return render(request, "auth/register.html", {"form": form})
def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        pwd = request.POST['password']
        user = authenticate(request, username=username, password=pwd)
        
        if user is not None:
            login(request, user)
            messages.success(request, "Vous êtes maintenant connecté !")
            return redirect("home")
        else:
            # Utilise Google Gemini pour générer un message d'erreur humoristique
            prompt_text = "Générer un seul message d'erreur humoristique et court pour un mot de passe incorrect."
            try:
                response = genai.GenerativeModel('gemini-1.5-flash').generate_content(prompt_text)
                error_message = response.text.strip() if hasattr(response, 'text') else "Mot de passe incorrect."
                
                

            except Exception as e:
                error_message = "Erreur lors de la génération d'un message d'erreur. Veuillez réessayer plus tard."
                print(f"Erreur avec Google Gemini : {e}")

            # Afficher le message d'erreur
            messages.error(request, error_message)
            return redirect("login")
        
    return render(request, 'auth/login.html')


        





