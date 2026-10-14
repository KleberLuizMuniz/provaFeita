from django.http import HttpResponse #ADICIONEI PARA CADASTRO

from django.shortcuts import render


def index(request):
    return render(
        request,
        'portal/index.html' #APAGUEI O "TEMPLATES/" DE "TEMPLATES/PORTAL/INDEX.HTML" QUE ESTAVA ANTES
    )

def cadastro(request): #CRIAÇÃO DO CADASTRO PARA URLS.PY FUNCIONAR
    return HttpResponse ("Ta aí bro") 
    
