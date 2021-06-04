from django.core.validators import MinValueValidator
from django.db import models

# Create your models here.
from django.utils.datetime_safe import datetime

class Moto(models.Model):
    venda = models.CharField(max_length=50, null=False)
    cliente = models.CharField(max_length=50, null=False)
    marca = models.CharField(max_length=50, null=False)
    ano = models.PositiveIntegerField(validators=[MinValueValidator(2005)], null=False)
    valor = models.FloatField(null=False)
    data_cadastro = models.DateTimeField(default=datetime.now(), null=False)
