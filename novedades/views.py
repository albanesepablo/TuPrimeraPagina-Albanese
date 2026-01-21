from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Novedad
from .forms import NovedadForm

class NovedadListView(ListView):
    model = Novedad
    template_name = 'novedades/novedad_list.html'
    context_object_name = 'novedades'

class NovedadDetailView(DetailView):
    model = Novedad
    template_name = 'novedades/novedad_detail.html'

class NovedadCreateView(LoginRequiredMixin, CreateView):
    model = Novedad
    form_class = NovedadForm
    template_name = 'novedades/novedad_form.html'
    success_url = reverse_lazy('novedades_lista')

class NovedadUpdateView(LoginRequiredMixin, UpdateView):
    model = Novedad
    form_class = NovedadForm
    template_name = 'novedades/novedad_form.html'
    success_url = reverse_lazy('novedades_lista')

class NovedadDeleteView(LoginRequiredMixin, DeleteView):
    model = Novedad
    template_name = 'novedades/novedad_confirm_delete.html'
    success_url = reverse_lazy('novedades_lista')
