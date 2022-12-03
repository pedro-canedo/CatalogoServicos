from audioop import reverse
from django.db import models
from django.contrib.auth import get_user_model

class Task(models.Model):

    COMPLEXIDADE = (
        ('baixa', 'Baixa'),
        ('media', 'Média'),
        ('alta', 'Alta'),
    )
    
    PERFIL = (
        ('não definido', 'Não definido'),
        ('junior', 'Junior'),
        ('pleno', 'Pleno'),
        ('senior', 'Senior'),
    )
    
    def define_tempo_sugerido(complexidade):
        complexidade = str(complexidade)
        complexidade = complexidade.lower()
        if complexidade == 'baixa':
            return (
                ('Até 2 horas', 'Até 2 horas'),
                ('Até 5 horas', 'Até 5 horas'),
                ('Até 10 horas', 'Até 10 horas'),
            )
        elif complexidade == 'media':
            return (
                ('Até 15 horas', 'Até 15 horas'),
                ('Até 20 horas', 'Até 20 horas'),
                ('Até 30 horas', 'Até 30 horas'),
                
            )
        elif complexidade == 'alta':
            return (
                ('Até 40 horas', 'Até 40 horas'),
                ('Até 50 horas', 'Até 50 horas'),
                ('Até 60 horas', 'Até 60 horas'),
            )
        
    

    nome = models.CharField(max_length=255)
    
    complexidade = models.CharField(max_length=100, choices=COMPLEXIDADE, default='baixa', blank=True, error_messages={'required': 'Por favor, selecione uma opção.'})
    
    escopo = models.CharField(max_length=255)
    
    tempo_limite = models.CharField(max_length=100, default=define_tempo_sugerido(complexidade), blank=True)
    
    entregaveis = models.CharField(max_length=255)
    
    perfil_exigido = models.CharField(max_length=100, choices=PERFIL, default='não definido', blank=True, error_messages={'required': 'Por favor, selecione uma opção.'})
    
    atividades_desempenhadas = models.CharField(max_length=255)
    
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome
    
    
class Atividades(models.Model):
    nome = models.CharField(max_length=255)
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome

    
 