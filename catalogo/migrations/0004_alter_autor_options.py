# Generated by Django 4.0 on 2022-01-10 20:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0003_alter_exemplarlivro_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='autor',
            options={'ordering': ['ultimo_nome', 'primeiro_nome'], 'permissions': (('pode_manipular_autor', 'Manipula o cadastro de autores.'),)},
        ),
    ]
