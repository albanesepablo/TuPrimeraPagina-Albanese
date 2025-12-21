from django.shortcuts import render
from ferreteria.models import Sector

def home(request):
    return render(request, 'ferreteria/index.html')



def listar_sectores(request):
    sectores_query = Sector.objects.all() # list(QuerySet[Sector, ..., Sector, ...])
    contexto = {
        'sectores':sectores_query
    }
    return render(request, 'ferreteria/sectores.html', contexto)