from django.contrib import admin

from .models import Filme
@admin.register(Filme)
class FilmeAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'diretor', 'genero', 'ano_lancamento', 'duracao')
    search_fields = ('titulo', 'diretor', 'genero')
    list_filter = ('genero', 'ano_lancamento')
