from django.contrib.auth.models import User
from django.db import models

class Pessoa(models.Model):
	nome = models.CharField('Nome', max_length=128, blank=True, null=True)
	email = models.EmailField('E-mail', blank=True, null=True)
	

	class Meta:
		verbose_name='Pessoa'
		verbose_name_plural='Pessoas'

	def __str__(self):
		return self.nome

class PessoaFisica(models.Model):
	pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
	cpf = models.CharField('CPF', max_length=128, blank=True, null=True)
	

	class Meta:
		verbose_name='Pessoa Fisica'
		verbose_name_plural='Pessoa Fisica'

	def __str__(self):
		return self.cpf

class Evento(models.Model):
	nome = models.CharField('Nome', max_length=128, blank=True, null=True)
	sigla = models.CharField('Sigla', max_length=128, blank=True, null=True)
	data_inicio = models.DateField(blank=True, null=True)
	realizador = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
	descricao = models.TextField()
	

	class Meta:
		verbose_name='Evento'
		verbose_name_plural='Eventos'

	def __str__(self):
		return self.nome

class Ingresso(models.Model):
	descricao = models.TextField()
	valor = models.FloatField('Valor', blank=True, null=True)
	realizador = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
	descricao = models.TextField()
	

	class Meta:
		verbose_name='Ingresso'
		verbose_name_plural='Ingressos'

	def __str__(self):
		return self.descricao

class Inscricao(models.Model):
	pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
	evento = models.ForeignKey(Evento, on_delete=models.CASCADE)
	ingresso = models.ForeignKey(Ingresso, on_delete=models.CASCADE)
	

	class Meta:
		verbose_name='Inscrição'
		verbose_name_plural='Inscrições'
