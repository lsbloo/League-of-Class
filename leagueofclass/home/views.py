from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import *
from django.shortcuts import redirect
from .form import UsuarioForm
from django.contrib import messages

# Create your views here.


def createAuthentic(request):
	# Responsavel por criar a autenticaçao do usuario!

	if request.method == "POST":
		form = UsuarioForm(request.POST)
		if form.is_valid():
			# Pegar os dados do formulario da pagina inicial!
			object_user = User.objects.get(email=form.cleaned_data['email'])
			user_aut = authenticate(username=object_user.username,password=form.cleaned_data['senha'])
			if user_aut is not None:
				login(request,user_aut)
				return redirect('/dashborad')
			else:
				messages.warning(request, 'Preencha todos os campos corretamente!')
				return redirect('/asgagsyas')
	else:
		form = UsuarioForm()


	return render(request,'index.html',  {'form':form})
