from django.shortcuts import render
from .models import Aluno,Professor
from .form import ProfessorForm,AlunoForm;
from django.views.generic.edit import CreateView
from django.shortcuts import redirect
from django.contrib import messages
from time import sleep
# Create your views here.


def cadastroProfessor(request):
	#url cadastro/ retorna o template de cadastros Professor!
	#Ñ implementada ainda;
	
	if request.method=="POST":
		form = ProfessorForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, 'Dados cadastrados com sucesso!')
			sleep(1)
			return redirect('/home')
		else:
			messages.warning(request, 'Preencha todos os campos corretamente!')
			
	else:
		form = ProfessorForm()
	return render(request,'leagueofclass/cadastroprofessor.html' , {'form':form})

dados_aluno_necessario={}
def cadastroAluno(request):
	if request.method=="POST":
		form = AlunoForm(request.POST)
		'''
		dados_aluno_necessario['nome'] = request.POST.get('nome')
		dados_aluno_necessario['sexo'] = request.POST.get('sexo')
		dados_aluno_necessario['dataNascimento'] = request.POST.get('dataNascimento')
		dados_aluno_necessario['email'] = request.POST.get('email')
		dados_aluno_necessario['login'] = request.POST.get('login')
		dados_aluno_necessario['password'] = request.POST.get('senha')
		dados_aluno_necessario['nomeInstituicao'] = request.POST.get('nomeInstituicao')
		'''

		if form.is_valid():
			form.save();
			sleep(1)
			return redirect('/home')
	else:
		form = AlunoForm()


	return render(request,'leagueofclass/cadastroaluno.html', {'form':form})

