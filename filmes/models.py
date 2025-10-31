from django.db import models

class Filme(models.Model):
    titulo = models.CharField(max_length=100)
    diretor = models.CharField(max_length=100)
    genero = models.CharField(max_length=50)
    ano_lancamento = models.PositiveIntegerField()
    duracao = models.PositiveIntegerField()
    sinopse = models.TextField(blank=True)
    poster = models.ImageField(upload_to='posters/', blank=True, null=True)

    def __str__(self):
        return self.titulo
