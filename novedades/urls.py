from django.urls import path
from .views import (
    NovedadListView,
    NovedadDetailView,
    NovedadCreateView,
    NovedadUpdateView,
    NovedadDeleteView,
)

urlpatterns = [
    path('', NovedadListView.as_view(), name='novedades_lista'),
    path('<int:pk>/', NovedadDetailView.as_view(), name='novedad_detalle'),
    path('crear/', NovedadCreateView.as_view(), name='novedad_crear'),
    path('editar/<int:pk>/', NovedadUpdateView.as_view(), name='novedad_editar'),
    path('borrar/<int:pk>/', NovedadDeleteView.as_view(), name='novedad_borrar'),
]
