from django.contrib import admin
from .models import *
# Register your models here.


# PERMISSAO MAXIMA DE ACESSO PODE REMOVER QUAL OBJECT DA CLASSE MODEL CAD;
# LOGIN: lsbloo
# SENHA : lsbloo6036236
'''
 # comando para criar um Super USer especifico
 ## python3 manage.py createsuperser
   -> necessita: username: !! , email: !! , password: !! 
'''
admin.site.register(Cpf)
admin.site.register(Pessoa)
admin.site.register(Professor)
admin.site.register(Aluno)
admin.site.register(Notas)
admin.site.register(Disciplinas)
