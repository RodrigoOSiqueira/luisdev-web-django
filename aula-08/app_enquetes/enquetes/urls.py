from django.urls import path

from . import views


urlpatterns = [
    path("", views.lista_enquetes, name="lista"),
    path("<int:id_enquete>/", views.detalhe_enquete, name="detalhe"),
]