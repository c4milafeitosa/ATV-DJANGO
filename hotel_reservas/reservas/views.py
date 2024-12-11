from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Quarto, Reserva
from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = 'index.html'

class QuartoListView(ListView):
    model = Quarto
    template_name = 'quarto_list.html'

class QuartoDetailView(DetailView):
    model = Quarto
    template_name = 'quarto_detail.html'

class QuartoCreateView(CreateView):
    model = Quarto
    fields = ['numero', 'tipo', 'preco']
    template_name = 'quarto_form.html'
    success_url = reverse_lazy('quarto_list')

class QuartoUpdateView(UpdateView):
    model = Quarto
    fields = ['numero', 'tipo', 'preco']
    template_name = 'quarto_form.html'
    success_url = reverse_lazy('quarto_list')

class QuartoDeleteView(DeleteView):
    model = Quarto
    template_name = 'quarto_confirm_delete.html'
    success_url = reverse_lazy('quarto_list')

class ReservaListView(ListView):
    model = Reserva
    template_name = 'reserva_list.html'

class ReservaDetailView(DetailView):
    model = Reserva
    template_name = 'reserva_detail.html'

class ReservaCreateView(CreateView):
    model = Reserva
    fields = ['quarto', 'data_inicio', 'data_termino', 'nome_cliente']
    template_name = 'reserva_form.html'
    success_url = reverse_lazy('reserva_list')

class ReservaUpdateView(UpdateView):
    model = Reserva
    fields = ['quarto', 'data_inicio', 'data_termino', 'nome_cliente']
    template_name = 'reserva_form.html'
    success_url = reverse_lazy('reserva_list')

class ReservaDeleteView(DeleteView):
    model = Reserva
    template_name = 'reserva_confirm_delete.html'
    success_url = reverse_lazy('reserva_list')

