from django.contrib import admin
from .models import Ingresso
from .models import Evento
from .models import Inscricao
from .models import Pessoa
from .models import PessoaFisica

# Register your models here.
@admin.register(Pessoa, PessoaFisica, Ingresso, Inscricao, Evento)
class EventoAdmin(admin.ModelAdmin):
	pass
class PessoaAdmin(admin.ModelAdmin):
	pass
class PessoaFisicaAdmin(admin.ModelAdmin):
	pass
class IngressoAdmin(admin.ModelAdmin):
	pass
class InscricaoAdmin(admin.ModelAdmin):
	pass