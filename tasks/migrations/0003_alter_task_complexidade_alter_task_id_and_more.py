# Generated by Django 4.1.3 on 2022-12-01 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_alter_task_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='complexidade',
            field=models.CharField(blank=True, choices=[('baixa', 'Baixa'), ('media', 'Média'), ('alta', 'Alta')], default='baixa', error_messages={'required': 'Por favor, selecione uma opção.'}, max_length=100),
        ),
        migrations.AlterField(
            model_name='task',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='task',
            name='tempo_limite',
            field=models.CharField(max_length=255),
        ),
    ]
