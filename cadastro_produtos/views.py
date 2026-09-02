from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from .models import Produtos


@login_required(login_url='login')
def cadastro_produtos(request):
    if request.method == 'POST':
        produto = request.POST.get('produto')
        preco = request.POST.get('preco')
        descricao = request.POST.get('descricao')
        categoria = request.POST.get('categoria')

        if Produtos.objects.filter(produto=produto).exists():
            return render(request, 'produtos/cadastro_produtos.html', {'mensagem': 'Produto já cadastrado!'})



        
        Produtos_db = Produtos.objects.create(produto=produto, preco=preco, descricao=descricao, categoria=categoria)
        Produtos_db.save()
        
        return redirect('cadastro_produtos',)
    produtos_lista = Produtos.objects.all()
    return render(request, 'produtos/cadastro_produtos.html', {'produtos_lista': produtos_lista})

def deletar_produto(request, id):
    id_produto = get_object_or_404(Produtos, pk=id)
    id_produto.delete()
    
    return redirect('cadastro_produtos')
# Create your views here.
