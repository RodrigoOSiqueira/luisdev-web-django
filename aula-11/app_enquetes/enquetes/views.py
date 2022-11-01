from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Enquete, Escolha
from .services.escolha_service import EscolhaService


@login_required()
def lista_enquetes(request: HttpRequest) -> HttpResponse:
    enquetes = Enquete.objects.all().order_by("texto")

    return render(request, "enquetes/lista.html", {"enquetes": enquetes})


@login_required()
def detalhe_enquete(request: HttpRequest, id_enquete: int) -> HttpResponse:
    """
        Essa é uma forma de pegar um objecto específico com o filter
        enquetes = Enquete.objects.filter(id=id_enquete)

        if not enquetes:
            return HttpResponse("Você não passou um id valido")

        enquete = enquetes.first()
    """
    try:
        enquete = Enquete.objects.get(id=id_enquete)
    except Enquete.DoesNotExist as e:
        print(f"[Erro]: {e}")
        enquetes = Enquete.objects.all().order_by("texto")
        context = {
            "enquetes": enquetes,
            "erro": f"Você tentou acessar uma enquete que não existe. Id: {id_enquete}"
        }

        return render(request, "enquetes/lista.html", context)

    return render(request, "enquetes/detalhe.html", {"enquete": enquete})


@login_required()
def votar(request: HttpRequest, id_enquete: int) -> HttpResponse:
    enquete = Enquete.objects.get(id=id_enquete)
    escolha_id = request.POST.get("escolha_id")

    if not escolha_id:
        contexto = {
            "enquete": enquete,
            "erro": "Você precisa selecionar uma escolha"
        }
        return render(request, "enquetes/detalhe.html", contexto)

    escolha_service = EscolhaService(escolha_id)
    escolha_service.vote()

    return HttpResponseRedirect(reverse('enquetes:resultados', args=(id_enquete,)))


@login_required()
def resultados(request: HttpRequest, id_enquete: int) -> HttpResponse:
    enquete = Enquete.objects.get(id=id_enquete)

    return render(request, "enquetes/resultados.html", {"enquete": enquete})
