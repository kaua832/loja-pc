from django.shortcuts import render
from .models import Compras

# Create your views here.
from django.shortcuts import render
from .models import Compras  # Importa a sua classe Compras

def carrinho(request):
    # Busca todas as compras salvas no banco de dados
    todas_as_compras = Compras.objects.all()
    
    # Prepara o contexto para enviar os dados para o HTML
    contexto = {
        'compras': todas_as_compras
    }
    
    # Renderiza a página do carrinho enviando as informações
    return render(request, 'home/carrinho.html', contexto)