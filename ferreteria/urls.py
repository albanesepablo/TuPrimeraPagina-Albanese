from django.urls import path
from ferreteria.views import *


urlpatterns = [
    path('', home, name='home')
]