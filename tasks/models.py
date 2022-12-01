from django.db import models
from django.contrib.auth import get_user_model

class Task(models.Model):

    COMPLEXIDADE = (
        ('baixa', 'Baixa'),
        ('media', 'Média'),
        ('alta', 'Alta'),
    )
    

    nome = models.CharField(max_length=255)
    complexidade = models.CharField(max_length=100, choices=COMPLEXIDADE, default='baixa', blank=True, error_messages={'required': 'Por favor, selecione uma opção.'})
    escopo = models.CharField(max_length=255)
    tempo_limite = models.CharField(max_length=255)
    entregaveis = models.CharField(max_length=255)
    perfil_exigido = models.CharField(max_length=255)
    atividades_desempenhadas = models.CharField(max_length=255)
    
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome
