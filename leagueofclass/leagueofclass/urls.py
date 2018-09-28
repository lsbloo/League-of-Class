
"""leagueofclass URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from cadastros.views import cadastroProfessor,cadastroAtividade
from cadastros.views import cadastroAluno
from cadastros.views import createAuthentic
from acessos.views import chosePerfil
from acessos.views import acessoProfessor
from acessos.views import acessoAluno
from acessos.views import notasAluno
from acessos.views import frequnciaAluno
from acessos.views import atividadesAluno
from acessos.views import clickMe
from cadastros.views import cadastroDisciplinaAluno
from acessos.views import logoutUser
from acessos.views import failUserXFF

# URLS PRE DEFINIDAS 
'''
	# URLS!
	> /INDEX
	/
	/home
	/admin
	/login
	/cadastroAluno
	/cadastroProfessor
	/escolherPerfil
	/logout
	/dashboardProfessor
	/dashboardAluno

	SUB_URLS:
		/relatoriosProfessor
		/relatoriosAluno
'''
urlpatterns = [
    path('admin/', admin.site.urls),
    path('escolherPerfil/',chosePerfil),
    path('', clickMe),
    path('home/', createAuthentic),
    path('index/', createAuthentic),
    path('cadastroProfessor/', cadastroProfessor),
    path('cadastroAluno/',cadastroAluno),
    path('dashboardAluno/',acessoAluno),
    path('dashboardProfessor/',acessoProfessor),
    path('cadastroAtividade/',cadastroAtividade),
    path('dashboardAluno/notas/', notasAluno),
    path('dashboardAluno/disciplinas', cadastroDisciplinaAluno),
    path('dashboardAluno/frequencia', frequnciaAluno),
    path('dashboardAluno/atividades', atividadesAluno),
    path('logout/',logoutUser),
    path('failUser/',failUserXFF)


]
