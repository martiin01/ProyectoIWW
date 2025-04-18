# Generated by Django 5.0.3 on 2025-04-08 17:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categoria', '0001_initial'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_Categoria', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('idCategoria', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='user.user')),
            ],
        ),
        migrations.DeleteModel(
            name='Producto',
        ),
    ]
