from django import forms
from .models import Produto


class ContatoForm(forms.Form):
    nome = forms.CharField(label='Nome', max_length=100)
    email = forms.EmailField(label='E-mail', max_length=100)
    assunto = forms.CharField(label='Assunto', max_length=120)
    msg = forms.CharField(label='Mensagem', widget=forms.Textarea())


class ProdutoModelForm(forms.ModelForm):

    class Meta:
        model = Produto
        fields = ['nome', 'preco', 'estoque', 'imagem']
