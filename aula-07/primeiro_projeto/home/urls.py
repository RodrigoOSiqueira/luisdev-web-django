from django.urls import path

from . import views


urlpatterns = [
    path('', views.home, name='my-home'),
    path('the-project-two', views.project, name='the-project'),
    path('the-crew', views.the_crew, name='the-crew'),
    path('contact', views.contact, name='contact'),
]
