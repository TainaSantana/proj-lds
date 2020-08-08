from django import forms

from .models import Reuniao

class MeetForm(forms.ModelForm):

    class Meta:
        model = Reuniao
        fields = ('titulo', 'data_inicio', 'data_fim', 'descricao', 'pauta', 'email')

class ContactForm(forms.Form):
    fromemail = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(required=True)
