from django.shortcuts import render
from cadastro_produtos.models import Produtos

# Create your views here.
def home(request):
    produtos = Produtos.objects.all()
    return render(request, 'home/loja.html', {'produtos': produtos})

