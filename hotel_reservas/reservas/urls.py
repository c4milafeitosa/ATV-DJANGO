from django.urls import path
from .views import (
    IndexView, QuartoListView, QuartoDetailView, QuartoCreateView, QuartoUpdateView, QuartoDeleteView,
    ReservaListView, ReservaDetailView, ReservaCreateView, ReservaUpdateView, ReservaDeleteView
)

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('quartos/', QuartoListView.as_view(), name='quarto_list'),
    path('quartos/<int:pk>/', QuartoDetailView.as_view(), name='quarto_detail'),
    path('quartos/novo/', QuartoCreateView.as_view(), name='quarto_create'),
    path('quartos/<int:pk>/editar/', QuartoUpdateView.as_view(), name='quarto_update'),
    path('quartos/<int:pk>/excluir/', QuartoDeleteView.as_view(), name='quarto_delete'),
    path('reservas/', ReservaListView.as_view(), name='reserva_list'),
    path('reservas/<int:pk>/', ReservaDetailView.as_view(), name='reserva_detail'),
    path('reservas/novo/', ReservaCreateView.as_view(), name='reserva_create'),
    path('reservas/<int:pk>/editar/', ReservaUpdateView.as_view(), name='reserva_update'),
    path('reservas/<int:pk>/excluir/', ReservaDeleteView.as_view(), name='reserva_delete'),
]
