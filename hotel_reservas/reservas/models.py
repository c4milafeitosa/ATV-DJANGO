from django.db import models
from django.core.exceptions import ValidationError
from django.urls import reverse


class Quarto(models.Model):
    numero = models.CharField(max_length=10, unique=True)
    tipo = models.CharField(max_length=50)
    preco = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Quarto {self.numero} - {self.tipo}"
    
    def get_absolute_url(self):
        return reverse('quarto_detail', args=[str(self.id)])


class Reserva(models.Model):
    quarto = models.ForeignKey(Quarto, on_delete=models.CASCADE, related_name='reservas')
    data_inicio = models.DateField()
    data_termino = models.DateField()
    nome_cliente = models.CharField(max_length=100)

    def __str__(self):
        return f"Reserva de {self.nome_cliente} ({self.data_inicio} - {self.data_termino})"

    def get_absolute_url(self):
        return reverse('reserva_detail', args=[str(self.id)])
    
    def clean(self):
        if self.data_termino < self.data_inicio:
            raise ValidationError('A data de término deve ser posterior à data de início.')