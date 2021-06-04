from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^cadastrar_moto/', cadastrar_moto, name='cadastrar_moto'),
    url(r'^listar_moto/', listar_moto, name='moto_list'),
    url(r'^editar_moto/(?P<pk>[0-9]+)', editar_moto, name='editar_moto'),
    url(r'^remover_moto/(?P<pk>[0-9]+)', remover_moto, name='remover_moto'),
]