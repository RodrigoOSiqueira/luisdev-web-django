from django import forms

from ..constants import ESCOLHAS_GENERO, ESCOLHAS_ESTADO


class ProfileForm(forms.Form):
    """Bloco user default"""
    username = forms.CharField(label="Nome de usuário", max_length=255)
    senha = forms.CharField(label="Senha", max_length=255)
    senha_2 = forms.CharField(label="Confirmação de senha", max_length=255)
    email = forms.EmailField(label="Email")
    nome = forms.CharField(label="Nome", max_length=255, required=False)
    sobrenome = forms.CharField(label="Sobrenome", max_length=255, required=False)

    """Bloco dados pessoais"""
    idade = forms.IntegerField(label="Idade", required=False)
    genero = forms.ChoiceField(label="Gênero", required=False)
    bio = forms.CharField(label="Descrição", max_length=500)
    profissao = forms.CharField(label="Profissão", max_length=255, required=False)

    """Bloco de endereço"""
    endereco = forms.CharField(label="Endereço", max_length=255, required=False)
    numero = forms.CharField(label="Número", max_length=50, required=False)
    cep = forms.CharField(label="CEP", max_length=50, required=False)
    cidade = forms.CharField(label="Cidade", max_length=100, required=False)
    estado = forms.ChoiceField(label="Estado", required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields["senha"].widget.input_type = "password"
        self.fields["senha_2"].widget.input_type = "password"

        self.fields["estado"].choices = ESCOLHAS_ESTADO
        self.fields["genero"].choices = ESCOLHAS_GENERO

        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})

        self.fields["estado"].widget.attrs.update({'class': 'form-select'})
        self.fields["genero"].widget.attrs.update({'class': 'form-select'})
