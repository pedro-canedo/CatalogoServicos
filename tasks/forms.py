from django import forms

from .models import Task

class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ('nome', 'complexidade', 'escopo', 'tempo_limite', 'entregaveis', 'perfil_exigido', 'atividades_desempenhadas')
        
        