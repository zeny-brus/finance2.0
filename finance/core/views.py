from django.shortcuts import render, redirect
from .models import Conta,Categoria
from django.contrib.messages import constants
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'home.html')

def gerenciar(request):
    contas = Conta.objects.all()
    categorias = Categoria.objects.all()

    return render (request, 'gerenciar.html', {'contas': contas})

def cadastrar_banco(request):
    apelido = request.POST.get('apelido')
    banco = request.POST.get('banco')
    tipo = request.POST.get('tipo')
    valor = request.POST.get('valor')
    icone = request.POST.get('icone')

    if len(apelido.strip()) == 0 or len(valor.strip()) == 0:
        messages.add_message(request, constants.ERROR, 'Preencha todos os campos')
        return redirect ('/gerenciar/')
    conta = Conta (
        apelido = apelido,
        banco = banco,
        tipo = tipo,
        valor = valor,
        icone = icone,
    )

    conta.save()
    messages.add_message(request, constants.SUCCESS,'conta cadastradas com sucesso')
    return redirect ('/gerenciar/')

def deletar_banco(request, id):
    conta = Conta.objects.get(id=id)
    conta.delete()

    messages.add_message(request, constants.SUCCESS, 'Conta removida com sucesso')
    return redirect('gerenciar/')