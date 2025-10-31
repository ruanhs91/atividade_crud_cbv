from django import forms
from .models import Filme 

class FilmeForm(forms.ModelForm):
    class Meta:
        model = Filme
        fields = ['titulo', 'diretor', 'genero', 'ano_lancamento', 'duracao', 'sinopse', 'poster']

    