from django.contrib.auth import authenticate, login, logout
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from common.constants import HTTPMethod

from .forms.profile_form import ProfileForm


def login_view(request: HttpRequest) -> HttpResponse:
    if request.method == HTTPMethod.GET:
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse("home:home"))

        return render(request, "accounts/login.html")
    
    username = request.POST.get("username")
    password = request.POST.get("password")

    user = authenticate(request, username=username, password=password)

    if not user:
        contexto = {"erro": "Nome de usuário ou senha inválidos"}
        return render(request, "accounts/login.html", contexto)

    login(request, user)
    return HttpResponseRedirect(reverse("home:home"))


def logout_view(request: HttpRequest) -> HttpResponse:
    logout(request)

    return HttpResponseRedirect(reverse("accounts:login"))


def criar_usuario(request: HttpRequest) -> HttpResponse:
    form = ProfileForm

    return render(request, "accounts/cadastro.html", {"form": form})
