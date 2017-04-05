from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import User


# Definiendo clase userForm
class UserForm(UserCreationForm):

	class Meta:
		model = User

		fields = [
			'username',
			'first_name',
			'last_name',
			'email',
			'is_active',
		]
		labels = {
			'username': 'Nombre de usuario',
			'first_name': 'Nombre',
			'last_name': 'Apellido',
			'email': 'Email',
			'is_active': 'Activar usuario',
		}
		widgets = {
			'username': forms.TextInput(attrs={'class': 'validate'}),
			'last_name': forms.TextInput(attrs={'class': 'validate'}),
			'email': forms.EmailInput(attrs={'class': 'validate'}),
			'first_name': forms.TextInput(attrs={'class': 'validate'}),
			'is_active': forms.HiddenInput(attrs={'value': 0}),
		}

	def clean(self):
		datos = self.cleaned_data
		for dato in datos:
			if dato == None:
				raise forms.ValidatonError('El campo ' + dato + 'no puede estar vacio')
		return datos