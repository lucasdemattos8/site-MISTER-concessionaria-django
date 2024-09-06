from django.db import models
from uuid import uuid4
import os
from django.utils.text import slugify

def upload_foto_carro(instance, filename):
    # Obtenha a extensão do arquivo
    ext = filename.split('.')[-1]
    slug = slugify(instance.carro_id)
    slug = slug[:50]
    new_filename = f"{slug}.{ext}"
    return os.path.join('carros', new_filename)

class Carro(models.Model):
    STATUS_CARROS = (
        ('V', 'Velho'),
        ('N', 'Novo'),
        ('U', 'Usado'),
    )
    
    CAMBIO_CHOICES = (
        ('M', 'Manual'),
        ('A', 'Automático'),
        ('S', 'Semi-automático'),
    )
    
    COMBUSTIVEL_CHOICES = (
        ('G', 'Gasolina'),
        ('A', 'Álcool'),
        ('D', 'Diesel'),
        ('F', 'Flex'),
        ('E', 'Elétrico'),
        ('H', 'Híbrido'),
    )

    carro_id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    carro_marca = models.CharField(max_length=60)
    carro_modelo = models.CharField(max_length=120)
    carro_ano = models.IntegerField()
    carro_cor = models.CharField(max_length=30)
    carro_valor = models.DecimalField(max_digits=10, decimal_places=2)
    carro_status = models.CharField(max_length=1, choices=STATUS_CARROS)
    carro_foto = models.ImageField(upload_to=upload_foto_carro, blank=True, null=False)
    carro_cadastro_em = models.DateField(auto_now_add=True)
    
    # Novos campos
    carro_km = models.PositiveIntegerField()
    carro_cambio = models.CharField(max_length=1, choices=CAMBIO_CHOICES)
    carro_combustivel = models.CharField(max_length=1, choices=COMBUSTIVEL_CHOICES)
    carro_cidade = models.CharField(max_length=60)

    class Meta:
        verbose_name_plural = "Carros"

    def __str__(self):
        return f"{self.carro_marca} {self.carro_modelo} ({self.carro_ano})"
    