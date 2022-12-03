from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponse
from .forms import TaskForm
from django.contrib import messages

from .models import Task

@login_required
def lista_servicos(request):
    
    search = request.GET.get('search')
    
    if search:
        tasks = Task.objects.filter(complexidade__icontains=search)
    else:
        tasks = Task.objects.all()
    return render(request, 'tasks/list.html', 
        {'tasks':tasks})



@login_required
def filtra_por_perfil(request, perfil):
    tasks = Task.objects.filter(perfil=perfil)
    return render(request, 'tasks/list.html', {'tasks': tasks})


@login_required
def newTask(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('/')
    else:
        form = TaskForm()
        return render(request, 'tasks/addtask.html', {'form': form})

@login_required
def editTask(request, id):
    task = get_object_or_404(Task, pk=id)
    form = TaskForm(request.POST or None, instance=task)
    if form.is_valid():
        form.save()
        messages.success(request, 'Tarefa atualizada com sucesso!')
        return redirect('/')
    return render(request, 'tasks/addtask.html', {'form': form})

@login_required
def deleteTask(request, id):
    task = get_object_or_404(Task, pk=id)
    task.delete()
    messages.success(request, 'Tarefa excluída com sucesso!')
    return redirect('/')



