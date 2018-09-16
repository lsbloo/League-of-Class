from django import forms
from .models import Usuarios



class UsuarioForm(forms.ModelForm):
	'''
	Responsavel por criar o modelo do form de USers para autenticação!;
	'''
	class Meta:
		model = Usuarios
		fields = ['email','senha','matricula']


