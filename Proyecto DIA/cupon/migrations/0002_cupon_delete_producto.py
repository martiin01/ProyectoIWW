# Generated by Django 5.0.3 on 2025-04-10 15:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cupon', '0001_initial'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cupon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_Cupon', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('idCupon', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='user.user')),
            ],
        ),
        migrations.DeleteModel(
            name='Producto',
        ),
    ]
