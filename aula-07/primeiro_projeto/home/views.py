from django.shortcuts import render
from django.http import HttpResponse, HttpRequest


def home(request: HttpRequest) -> HttpResponse:
    context = {
        "titulo_bloco": "Home page Proteza",
        "text_bloco": (
            "O Proteza nasceu da visão que estudantes"
            " de programação tem em relação a natureza."
            " A ideia é proge-la para que ela nos proteja"
            "O Proteza nasceu da visão que estudantes"
            " de programação tem em relação a natureza."
            " A ideia é proge-la para que ela nos proteja"
            "O Proteza nasceu da visão que estudantes"
            " de programação tem em relação a natureza."
            " A ideia é proge-la para que ela nos proteja"
        )
    }
    return render(request, 'home.html', context)


def project(request: HttpRequest) -> HttpResponse:
    return render(request, 'project.html')


def the_crew(request: HttpRequest) -> HttpResponse:
    return render(request, 'the_crew.html')


def contact(request: HttpRequest) -> HttpResponse:
    return render(request, 'contact.html')
