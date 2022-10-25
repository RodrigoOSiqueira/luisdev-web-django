from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


def home(request: HttpRequest) -> HttpResponse:
    context = {
        "titulo": "Enquetes feed",
        "sub_titulo": "O seu site favorito de enquetes",
        "texto_explicativo": (
            "Aqui você encontrará enquetes criadas por pessoas reais, " 
            "tendo a chance de criar suas próprias enquestes e votar nelas!"
        )
    }
    return render(request, "home.html", context)
