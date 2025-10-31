from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Filme
from .forms import FilmeForm

class ListarFilme(ListView):
    model = Filme
    template_name = 'listar.html'
    context_object_name = 'filmes'

class DetalhesFilme(DetailView):
    model = Filme
    template_name = 'detalhe.html'
    context_object_name = 'filme'

class AdicionarFilme(CreateView):
    model = Filme
    form_class = FilmeForm
    template_name = 'form.html'
    success_url = reverse_lazy('filmes:listar')

class EditarFilme(UpdateView):
    model = Filme
    form_class = FilmeForm
    template_name = 'form.html'
    success_url = reverse_lazy('filmes:listar')

class DeletarFilme(DeleteView):
    model = Filme
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('filmes:listar')
