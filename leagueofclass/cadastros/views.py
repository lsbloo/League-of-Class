from django.shortcuts import render
from .models import Aluno,Professor

# Create your views here.



def cad(request):
	#url cadastro/ retorna o template de cadastros!
	#Ñ implementada ainda;
	return render(request,'cadastro.html');

