# Generated by Django 5.1.2 on 2024-11-01 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ruedas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Dureza', models.CharField(max_length=4)),
                ('Perfil', models.CharField(max_length=9)),
                ('Compuesto', models.CharField(max_length=15)),
                ('Talla', models.IntegerField()),
            ],
        ),
    ]
