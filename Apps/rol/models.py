from __future__ import unicode_literals

from django.db import models

class Rol(models.Model):
	rol = models.CharField('Tipo de rol', db_column='typeOfRol', unique=True, max_length=50)

	class Meta:
		managed = True
		db_table = 'Rol'

	def __str__(self):
		return '{}'.format(self.rol)
