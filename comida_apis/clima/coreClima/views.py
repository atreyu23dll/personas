import requests 
from django.shortcuts import render, redirect
from .forms import RegistroUsuarioForm

API_URL = "http://127.0.0.1:8000/api/personas/"

def home(request):
    try:
        response = requests.get(API_URL)
        response.raise_for_status()
        lista_personas = response.json()
    except requests.RequestException as e:
        print(f"Error fetching data from API: {e}")
        lista_personas = []

    return render(request, "coreClima/home.html", {"personas": lista_personas})

def registrar_usuario(request):
    if request.method == "POST":
        form = RegistroUsuarioForm(request.POST)
        nombre = request.POST.get('nombre')
        email = request.POST.get('email')
        
        if form.is_valid():
            data = {
                "nombre": nombre,
                "email": email
            }
            
            try:
                response = requests.post(API_URL, json=data)
                response.raise_for_status()
                return redirect('home')
            except requests.RequestException as e:
                print(f"Error posting data to API: {e}")
                pass
    else:
        form = RegistroUsuarioForm()
    return render(request, "coreClima/registrar_usuario.html", {"form": form})
