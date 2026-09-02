from django.db import models

class Produtos(models.Model):
    produto = models.CharField(max_length=299)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    descricao = models.TextField()
    categoria = models.CharField(max_length=100)
# Create your models here.
