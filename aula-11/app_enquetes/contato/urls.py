from django.urls import path

from .import views


urlpatterns = [
    path('', views.ViewContato.as_view(), name='contato'),
]