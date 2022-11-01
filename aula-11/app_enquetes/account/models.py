from django.db import models
from django.conf import settings

from .constants import ESCOLHAS_GENERO, NAO_DECLARADO, ESCOLHAS_ESTADO


class Profile(models.Model):
    """
    Esse modelo usa da estratégia de user profile para estender o usuário default do DJANGO
    """
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    """Bloco dados pessoais"""
    idade = models.IntegerField(null=True)
    genero = models.CharField(
        max_length=100, 
        choices=ESCOLHAS_GENERO,
        null=True,
        default=NAO_DECLARADO,
    )
    bio = models.CharField(max_length=500)
    profissao = models.CharField(max_length=255, null=True)

    """Bloco de dados de endereços"""
    endereco = models.CharField(max_length=255, null=True)
    numero = models.CharField(max_length=50, null=True)
    cep = models.CharField(max_length=50, null=True)
    cidade = models.CharField(max_length=100, null=True)
    estado = models.CharField(max_length=3, choices=ESCOLHAS_ESTADO)
