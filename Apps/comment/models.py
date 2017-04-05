from django.db import models

from Apps.post.models import Post
from django.contrib.auth.forms import User

class State(models.Model):
	descr = models.CharField('Descripcion', blank=False, null=False, max_length=50)

	class Meta:
		managed = True
		db_table = 'Comment_State'

	def __str__(self):
		return '{}'.format(self.descr)

class Comment(models.Model):
	id_user = models.ForeignKey(User, db_column='id_user', blank=False, null=False, default=None)
	id_post = models.ForeignKey(Post, db_column='id_post', blank=False, null=False, default=None)
	text = models.TextField('Comentario', db_column='text', blank=False, null=False, max_length=300)
	created_at = models.DateTimeField('Fecha de comentario', db_column='created_at', blank=False, null=False, auto_now_add=True)
	current_state = models.ForeignKey(State, db_column='current_state', blank=False, null=False, default=True)

	class Meta:
		managed = True
		db_table = 'Comment'

	def __str__(self):
		return '{}'.format(self.id)