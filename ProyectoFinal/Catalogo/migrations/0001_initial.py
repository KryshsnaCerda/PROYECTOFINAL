# Generated by Django 4.1.2 on 2024-07-08 00:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id_genero', models.AutoField(db_column='idGenero', primary_key=True, serialize=False)),
                ('genero', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='cliente',
            fields=[
                ('correo', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=40)),
                ('aparterno', models.CharField(max_length=40)),
                ('amaterno', models.CharField(max_length=40)),
                ('contraseña', models.CharField(max_length=40)),
                ('id_genero', models.ForeignKey(db_column='idGenero', on_delete=django.db.models.deletion.CASCADE, to='Catalogo.genero')),
            ],
        ),
    ]
