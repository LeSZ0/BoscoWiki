from __future__ import unicode_literals

from django.db import models
from django import forms
from Apps.rol.models import Rol
from django.contrib.auth.forms import User

class User(models.Model):
    id_rol = models.ForeignKey(Rol, db_column='id_rol', default=2)  # Field name made lowercase.
    usuario = models.CharField(db_column='usuario', max_length=50, unique=True)  # Field name made lowercase.
    password = models.CharField('password', db_column='Pass', max_length=50)  # Field name made lowercase. Field renamed because it was a Python reserved word.
    email = models.EmailField(db_column='email', max_length=50, unique=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='nombre', max_length=50)  # Field name made lowercase.
    apellido = models.CharField(db_column='apellido', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'User'

    def __str__(self):
        return '{} {}'.format(self.nombre, self.apellido)
