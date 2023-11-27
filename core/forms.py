from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Reserva
from django.utils import timezone 

class CustomUserCreationForm(UserCreationForm):
    pass

class reservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['f_inicio', 'f_fin', 'hora_inicio', 'hora_fin', 'mascota', 'responsable', 'descrip']

        widgets = {
            'f_inicio': forms.DateInput(attrs={'type': 'date', 'format': '%Y-%m-%d', 'min': timezone.now().strftime('%Y-%m-%d')}),
            'f_fin': forms.DateInput(attrs={'type': 'date', 'format': '%Y-%m-%d', 'min': timezone.now().strftime('%Y-%m-%d')}),
            'hora_inicio': forms.TimeInput(attrs={'type': 'time', 'format': '%H:%M'}),
            'hora_fin': forms.TimeInput(attrs={'type': 'time', 'format': '%H:%M'}),
        }