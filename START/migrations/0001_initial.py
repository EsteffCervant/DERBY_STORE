# Generated by Django 5.1.2 on 2024-10-17 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patines',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Deporte', models.CharField(max_length=22)),
                ('Marca', models.CharField(max_length=18)),
                ('Talla', models.IntegerField()),
            ],
        ),
    ]