from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

from .models import Enquete, Escolha


def lista_enquetes(request: HttpRequest) -> HttpResponse:
    enquetes = Enquete.objects.all().order_by("texto")

    return render(request, "enquetes/lista.html", {"enquetes": enquetes})

def detalhe_enquete(request: HttpRequest, id_enquete: int) -> HttpResponse:
    emquete = Enquete.objects.get(id=id_enquete)
    return HttpResponse(f"Você esta vendo a enquete de id: {id_enquete}")
