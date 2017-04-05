from django import forms

from Apps.post.models import Post

# Definiendo clase userForm
class PostForm(forms.ModelForm):

	class Meta:
		model = Post

		fields = [
			'postTitle',
			'descr',
			'text',
			'id_user',
			'id_category',
			'files',
		]
		labels = {
			'postTitle': 'Titulo de la publicacion',
			'text': 'Contenido de la publicacion',
			'id_user': 'Usuario',
			'id_category': 'Categoria',
			'descr': 'Descripcion',
			'files': 'Sube tu imágen',
		}
		widgets = {
			'postTitle': forms.TextInput(attrs={'class': 'validate'}),
			'text': forms.Textarea(attrs={'class': 'validate materialize-textarea'}),
			'id_user': forms.Select(attrs={'class': 'validate'}),
			'id_category': forms.Select(attrs={'class': 'validate'}),
			'descr': forms.Textarea(attrs={'class': 'validate materialize-textarea'}),
		}