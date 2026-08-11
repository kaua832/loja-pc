from django.db import models
class Compras(models.Model):
    produtos = models.CharField(max_length=299)
    data_de_compra = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"compra em {self.data_de_compra}"
# Create your models here.
