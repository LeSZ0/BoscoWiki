from django import forms

from Apps.comment.models import Comment

class CommentForm(forms.ModelForm):

	class Meta:
		model = Comment

		fields = [
			'id_user',
			'id_post',
			'text',
			'current_state',
		]

		labels = {
			'id_user': 'Usuario',
			'id_post': 'Publicación',
			'text': 'Cuerpo del comentario',
			'current_state': 'Estado del comentario'
		}

		widgets = {
			'id_user': forms.Select(attrs={'class': 'validate'}),
			'id_post': forms.Select(attrs={'class': 'validate'}),
			'text': forms.Textarea(attrs={'class': 'validate'}),
			'current_state': forms.Select(attrs={'class': 'validate'}),
		}