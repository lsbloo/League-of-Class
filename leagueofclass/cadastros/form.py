from django import forms
from .models import Professor
from .models import Aluno
from django.forms import ModelForm



class ProfessorForm(ModelForm):
	'''
	Responsavel por criar o modelo de formulario a partir do modelo que esta sendo criado no db;
	'''

	class Meta:
		model = Professor
		fields = '__all__'



class AlunoForm(ModelForm):
	class Meta:
		model = Aluno
		fields = '__all__'
