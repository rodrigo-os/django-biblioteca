# Generated by Django 4.0 on 2022-01-10 19:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0002_exemplarlivro_usuario'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='exemplarlivro',
            options={'ordering': ['data_devolucao'], 'permissions': (('pode_renovar_emprestimo', 'Pode renovar empréstimo.'),)},
        ),
    ]
