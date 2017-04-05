from django import forms

from Apps.rol.models import Rol

# Definiendo clase userForm
class RolForm(forms.ModelForm):

	class Meta:
		model = Rol

		fields = [
			'rol',
		]
		labels = {
			'rol': 'Tipo de rol del usuario',
		}
		widgets = {
			'rol': forms.TextInput(attrs={'class': 'form-control'}),
		}