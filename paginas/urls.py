from django.urls import path
from .views import PaginaInicial, CatalogoTarefas

urlpatterns = [
    path('', PaginaInicial.as_view(), name='inicio'),
    ]