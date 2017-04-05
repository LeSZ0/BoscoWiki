from __future__ import unicode_literals

from django.db import models
#from Apps.user.models import User
from django.contrib.auth.forms import User

from ckeditor.fields import RichTextField

class Category(models.Model):
	name = models.CharField('Nombre', db_column='name', max_length=20, blank=False, null=False)

	class Meta:
		managed = True
		db_table = 'Category'

	def __str__(self):
		return '{}'.format(self.name)

# Create your models here.
class Post(models.Model):
    id_user = models.ForeignKey(User, db_column='id_user', blank=False, null=False) 
    postTitle = models.CharField('Titulo del post', db_column='titulo', max_length=60, blank=False, null=False)
    descr = models.TextField('Descripcion', db_column='descripcion', blank=True, null=True, max_length=60)
    text = models.TextField('Desarrollo', db_column='texto', blank=False, null=False, max_length=5000)
    id_category = models.ForeignKey(Category, db_column='id_category', blank=False, null=False, default=None)
    created_at = models.DateTimeField('Fecha de publicacion', db_column="created_at", auto_now_add=True, blank=True, null=False)
    files = models.ImageField('Archivos', db_column='files', default=None, null=True, blank=True)

    class Meta:
        managed = True
        db_table = 'Post'

    def __str__(self):
        return '{}'.format(self.postTitle)