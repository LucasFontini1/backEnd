from django.contrib import admin
from .models import aluno, matricula, turma, professores


admin.site.register(aluno)
admin.site.register(matricula)
admin.site.register(turma)
admin.site.register(professores)
# Register your models here.
