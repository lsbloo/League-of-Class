from django.shortcuts import render
from .models import Aluno,Professor

# Create your views here.



def cad(request):
	return render(request,'cadastro.html');

