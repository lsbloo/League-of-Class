from django import forms
from .models import Professor
from .models import Aluno
from .models import Usuarios
from .models import AtividadesProfessor


class AtividadeForm():
	'''
	Responsavel por criar uma Atividade q esta relacionada a um Professor
	Cada atividade precisa ter um Professor.
	uma Atividade pode ter Diversas Perguntas
	uma Atividade precisa de um titulo;
	'''
	class Meta:
		model = AtividadesProfessor
		fields = '__all__'

class ProfessorForm(forms.ModelForm):
	'''
	Responsavel por criar o modelo de formulario a partir do modelo que esta sendo criado no db;
	'''
	class Meta:
		model = Professor
		fields = ['nome', 'sexo','dataNascimento','email','login','password','nomeInstituicao', 'matricula']



class AlunoForm(forms.ModelForm):
	class Meta:
		model = Aluno
		#NÃO É PRECISO RECUPERAR TODOS OS FIELDS NESSE FORM O CADASTRO DE ALUNO, É MAIS SIMPLES QUE O DE PROFESSOR
		# É NECESSARIO O NOME DA INSTITUIÇÃO TAMBEM!
		#
		# form mais simples é isso #PAZ
		fields = [

		'nome', 'sexo','dataNascimento','email','login','password','nomeInstituicao',

			];



class UsuarioForm(forms.ModelForm):
	'''
	Responsavel por criar o modelo do form de USers para autenticação!;
	'''
	class Meta:
		model = Usuarios
		fields = ['email','senha','matricula']