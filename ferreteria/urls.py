from django.urls import path
from ferreteria.views import *


urlpatterns = [
    path('', home, name='home'),
    path('lista_sectores', listar_sectores, name='sector_list'),
]