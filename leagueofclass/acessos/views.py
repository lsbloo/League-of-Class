
import sys
sys.path.append('../')

from cadastros.models import Aluno
from django.shortcuts import render



def chosePerfil(request):
    return render(request,'leagueofclass/telaescolha.html')


def acessoProfessor(request):

    return render(request,'leagueofclass/painel_professor.html')

def acessoAluno(request):
    data = {}
    #ideia... fazer um filter que compare request.user com o usuário o login
    data['exibeInicio'] = True
    data['msg'] = 'Suas informações:'
    data['alunos'] = Aluno.objects.filter(login=request.user)
    data['usuario'] = request.user
    return render(request,'leagueofclass/painel_aluno.html', data)

def notasAluno(request):
    data = {}
    data['exibeNotas'] = True
    data['msg'] = 'Suas notas:'
    data['alunos'] = Aluno.objects.filter(login=request.user)
    return render(request,'leagueofclass/painel_aluno.html', data)

def disciplinasAluno(request):
    return render(request,'leagueofclass/painel_aluno.html')

def frequnciaAluno(request):
    return render(request,'leagueofclass/painel_aluno.html')

def atividadesAluno(request):
    return render(request,'leagueofclass/painel_aluno.html')