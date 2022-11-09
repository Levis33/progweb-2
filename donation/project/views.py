from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def home(request):
    context = {}
    return render(request, 'home.html', context=context)

def faq(request):
    context = {}
    return render(request, 'faq.html', context=context)

@login_required
def gerenciar_usuarios(request):
    context = {}
    return render(request, 'gerenciar_usuarios.html', context=context)

@login_required
def campanhas(request):
    context = {}
    return render(request, 'campanha.html', context=context)

@login_required
def criar_campanha(request):
    context = {}
    return render(request, 'criar_campanha.html', context=context)

@login_required
def editar_campanha(request):
    context = {}
    return render(request, 'editar_campanha.html', context=context)

@login_required
def doar_campanha(request, id_campanha):
    context = {}
    return render(request, 'doar_campanha.html', context=context)
