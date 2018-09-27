from django.db import models
import datetime
# Create your models here.
# Responsavel por criar os models do cad de professor e aluno





class Pessoa(models.Model):
		options_sexo=(('M','Masculino'),('F','Feminino'),('NDA','Qualquer Outro'))
		nome=models.CharField(max_length=60)
		sexo=models.CharField(max_length=1,choices=options_sexo)
		dataNascimento=models.DateField(("Data"), default=datetime.date.today)
		email=models.CharField(max_length=50)
		login=models.CharField(max_length=20)
		password=models.CharField(max_length=20);


class Professor(Pessoa):
	nomeInstituicao=models.CharField(max_length=30, primary_key=True)
	#codigo=models.CharField(max_length=10)

	#Adm deleta professor pela matricula;
	matricula=models.CharField(max_length=12)


class Aluno(Pessoa):
	nomeInstituicao=models.CharField(max_length=30,primary_key=True)
	descricaoDesempenho=models.CharField(max_length=150,blank=True)
	frequencia=models.CharField(max_length=40,blank=True)
	professor=models.ManyToManyField("Professor",blank=True);



class Notas(models.Model):
	primeiraUnidade=models.CharField(max_length=4)
	segundaUnidade=models.CharField(max_length=4)
	terceiraUnidade=models.CharField(max_length=4)
	media=models.CharField(max_length=4)

class Disciplinas(models.Model):
	nomeDisciplina=models.CharField(max_length=30)
	##descricaoDisciplina=models.CharField(max_length=120)
	professor = models.ForeignKey("Professor",on_delete=models.CASCADE)
	aluno = models.ForeignKey("Aluno",on_delete=models.CASCADE)


class Usuarios(models.Model):
    login=models.CharField(max_length=15)
    senha=models.CharField(max_length=12)
    email=models.CharField(max_length=50)
    matricula=models.CharField(max_length=12,blank=True)

class Perguntasx(models.Model):

   opcoes_alternativa_correta = \
   (
   ('A', 'Alternativa A'), ('B', 'Alternativa B'), ('C', 'Alternativa C'), ('D', 'Alternativa D')
   )
   ask=models.CharField(max_length=100,blank=False)
   alternativa_a = models.CharField(max_length=200,blank=False)
   alternativa_b = models.CharField(max_length=200,blank=False)
   alternativa_c = models.CharField(max_length=200,blank=False)
   alternativa_d = models.CharField(max_length=200,blank=False)
   alternativaCorreta = models.CharField(max_length=1,choices=opcoes_alternativa_correta)

class AtividadesProfessor(models.Model):
   titulo=models.CharField(max_length=200,primary_key=True)
   perguntas = models.ManyToManyField(Perguntasx)
   professor = models.OneToOneField("Professor",on_delete=models.CASCADE)
