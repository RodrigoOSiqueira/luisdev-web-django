from django.db import models

from common.models import BaseModel


class Enquete(BaseModel):
    texto = models.CharField(max_length=255, verbose_name="Texto da enquete")
    descricao = models.CharField(max_length=500, verbose_name="Descrição", null=True)
    data_pub = models.DateTimeField(verbose_name="Data de publicação", null=True)
    imagem = models.ImageField(upload_to="imagens_enquetes/", null=True, blank=True)

    def __str__(self):
        return f"#{self.id}.{self.texto}"


class Escolha(BaseModel):
    texto = models.CharField(max_length=200, verbose_name="Escolha")
    num_votos = models.IntegerField(default=0, verbose_name="Número de votos")
    enquete = models.ForeignKey(
        "Enquete", 
        on_delete=models.CASCADE,
        related_name="escolhas",
        verbose_name="Enquete"
    )
