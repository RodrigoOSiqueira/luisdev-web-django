from django.db import models


class BaseModel(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True, verbose_name="ID")
    criado_em = models.DateTimeField(auto_now_add=True)
    editado_em = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
