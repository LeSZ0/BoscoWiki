from django import forms

from django.contrib.auth.forms import User

class LoginForm(forms.ModelForm):

	class Meta:
		model = User

		fields = [
			'username',
			'password',
		]

		labels = {
			'username': 'Nombre de usuario',
			'password': 'Contraseña',
		}
		widgets = {
			'username': forms.TextInput(attrs={'class': 'validate'}),
			'password': forms.PasswordInput(attrs={'class': 'validate'}),
		}
