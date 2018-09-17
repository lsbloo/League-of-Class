
# Create your views here.

from django.shortcuts import render

def chosePerfil(request):
    return render(request,'leagueofclass/telaescolha.html')




def acessoProfessor(request):

    return render(request,'leagueofclass/painel_professor.html')

def acessoAluno(request):

    return render(request,'leagueofclass/painel_aluno.html')
