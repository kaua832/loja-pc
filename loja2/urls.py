"""
URL configuration for loja2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from loja_inicial import views as views_loja_inicial
from carrinho import views as views_carrinho
from login import views as views_login
from cadastro import views as views_cadastro
from painel import views as views_painel
from cadastro_produtos import views as views_produtos

urlpatterns = [
    path('admin/', admin.site.urls),
    path('carrinho/', views_carrinho.carrinho, name='carrinho'),
    path('login/', views_login.login_views, name='login'),
    path('cadastro/', views_cadastro.cadastro, name='cadastro'),
    path('ativar/<uidb64>/<token>/', views_cadastro.ativar_conta, name='ativar_conta'),
    path('', views_loja_inicial.home, name='home'),
    path('home/', views_loja_inicial.home, name='home'),
    path('logout/', views_login.logout_view, name='logout'),
    path('painel/', views_painel.painel, name='painel'),
    path('cadastro_produtos/', views_produtos.cadastro_produtos, name='cadastro_produtos'),
    path('deletar_produtos/<int:id>/', views_produtos.deletar_produto, name='deletar_produtos'),
    
]
