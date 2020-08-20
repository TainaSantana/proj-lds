from django import forms

from .models import Reuniao


class MeetForm(forms.ModelForm):
    
    class Meta:
        model = Reuniao
        fields = ('titulo', 'data_inicio', 'data_fim', 'descricao', 'pauta', 'email')




