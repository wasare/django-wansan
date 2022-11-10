from django.db import models

# Create your models here.
class Loja(models.Model):
    nome = models.CharField('Nome da Loja', max_length=64)
    pedido_minimo = models.DecimalField(
        'Pedido Mínimo',
        max_digits=5,
        decimal_places=2
    )


