from django.urls import path
from . import views 
app_name = 'filmes'

urlpatterns = [
    path('', views.ListarFilme.as_view(), name='listar'),
    path('filmes/<int:pk>/', views.DetalhesFilme.as_view(), name = 'detalhes'),
    path('criar/', views.AdicionarFilme.as_view(), name='adicionar'),
    path('editar/<int:pk>/', views.EditarFilme.as_view(), name='editar'),
    path('deletar/<int:pk>/', views.DeletarFilme.as_view(), name='deletar'),
]