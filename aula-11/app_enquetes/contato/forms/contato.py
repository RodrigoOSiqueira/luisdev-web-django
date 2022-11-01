from django import forms

from ..models import Contato


class FormContato(forms.ModelForm):
    class Meta:
        model = Contato
        fields = ['mensagem']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['mensagem'].widget.attrs.update({'class': 'form-control'})
        self.fields['mensagem'].help_text = 'Insira sua mensagem'
