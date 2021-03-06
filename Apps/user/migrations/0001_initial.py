# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-25 02:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('rol', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(db_column='usuario', max_length=50, unique=True)),
                ('password', models.CharField(db_column='Pass', max_length=50, verbose_name='password')),
                ('email', models.EmailField(db_column='email', max_length=50, unique=True)),
                ('nombre', models.CharField(db_column='nombre', max_length=50)),
                ('apellido', models.CharField(db_column='apellido', max_length=50)),
                ('id_rol', models.ForeignKey(db_column='id_rol', default=2, on_delete=django.db.models.deletion.CASCADE, to='rol.Rol')),
            ],
            options={
                'db_table': 'User',
                'managed': True,
            },
        ),
    ]
