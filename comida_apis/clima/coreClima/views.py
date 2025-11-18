import requests 
from django.shortcuts import render, redirect
from .forms import RegistroUsuarioForm
from .models import persona

def home(request):
    lista_personas = persona.objects.all()
    return render(request, "coreClima/home.html", {"personas": lista_personas})

def registrar_usuario(request):
    if request.method == "POST":
        form = RegistroUsuarioForm(request.POST)
        nombre = request.POST.get('nombre')
        email = request.POST.get('email')
        persona.objects.create(nombre=nombre, email=email)
        return redirect('home')
    else:
        form = RegistroUsuarioForm()
    return render(request, "coreClima/registrar_usuario.html", {"form": form})
