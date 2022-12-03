from django.urls import path

from . import views

urlpatterns = [
    path('', views.lista_servicos, name='task-list'),
    path('newtask/', views.newTask, name="new-task"),
    path('edit/<int:id>', views.editTask, name="edit-task"),
    path('delete/<int:id>', views.deleteTask, name="delete-task"),
]