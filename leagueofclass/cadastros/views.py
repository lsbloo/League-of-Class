from django.shortcuts import render
from .models import Aluno,Professor
from .form import ProfessorForm,AlunoForm;
from django.views.generic.edit import CreateView
from django.shortcuts import redirect
from django.contrib import messages
from time import sleep
from django.contrib.auth.models import User
from django.shortcuts import HttpResponseRedirect
from django.views.decorators.http import require_POST
# Create your views here.



def cadastroProfessor(request):
	#url cadastro/ retorna o template de cadastros Professor!
	#Ñ implementada ainda;

	
	if request.method=="POST":
		form = ProfessorForm(request.POST)

		if form.is_valid():

				try:

					verificaExistenciaPass = User.objects.get(password=form.cleaned_data['password'])
					verificaExistencia = User.objects.get(email=form.cleaned_data['email'])
					if verificaExistenciaPass or verificaExistencia:
						return render(request,'/home', {'msg': 'Ja existe um usuario com o mesmo email!'})


				except User.DoesNotExist:
					nome_professor = form.cleaned_data['nome']
					email_professor = form.cleaned_data['email']
					password_professor = form.cleaned_data['password']
					new_professor = User.objects.create_user(username=nome_professor, email=email_professor,
															 password=password_professor)

					new_professor.save()
					form.save()
					return redirect("/home")




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
			try:

				verificaExistenciaPass = User.objects.get(password=form.cleaned_data['password'])
				verificaExistencia = User.objects.get(email=form.cleaned_data['email'])
				if verificaExistenciaPass or verificaExistencia:
					return render(request, '/home', {'msg': 'Ja existe um usuario com o mesmo email!'})


			except User.DoesNotExist:
				nome_aluno = form.cleaned_data['nome']
				email_aluno = form.cleaned_data['email']
				password_aluno = form.cleaned_data['password']
				new_aluno = User.objects.create_user(username=nome_aluno, email=email_aluno,
														 password=password_aluno)

				new_aluno.save()
				form.save()
				return redirect("/home")
		else:
			messages.warning(request, 'Preencha todos os campos corretamente!')
	else:
		form = AlunoForm()


	return render(request,'leagueofclass/cadastroaluno.html', {'form':form})

