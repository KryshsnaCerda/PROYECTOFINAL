# Generated by Django 4.1.2 on 2024-07-09 22:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Catalogo', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='id_genero',
        ),
        migrations.DeleteModel(
            name='Genero',
        ),
    ]
