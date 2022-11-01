from django.conf import settings
from django.db import models

from common.models import BaseModel

from .constants import ESCOLHAS_STATUS


class Contato(BaseModel):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.SET_NULL,
        related_name="contatos",
        verbose_name="Usuário",
        null=True,
    )
    mensagem = models.TextField(verbose_name="Mensagem")
    status = models.CharField(max_length=255, verbose_name="Status", choices=ESCOLHAS_STATUS)

def __str__(self):
    return f"#{self.id}.{self.mensagem}"
