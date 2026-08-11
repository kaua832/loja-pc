from django.db import models

class Compras(models.Model):
    produtos = models.CharField(max_length=299)
    data_de_compra = models.DateTimeField(auto_now_add=True)
# Create your models here.
