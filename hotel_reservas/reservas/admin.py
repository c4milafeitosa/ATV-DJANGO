from django.contrib import admin
from .models import Quarto, Reserva

@admin.register(Quarto)
class QuartoAdmin(admin.ModelAdmin):
    list_display = ('numero', 'tipo', 'preco')

@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ('nome_cliente', 'data_inicio', 'data_termino', 'quarto')
