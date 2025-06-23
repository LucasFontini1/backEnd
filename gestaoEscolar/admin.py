from django.contrib import admin
from .models import aluno, matricula, turma, nota, frequencia, disciplina, professores, curso, coordenador


admin.site.register(aluno)
admin.site.register(matricula)
admin.site.register(turma)
admin.site.register(nota)
admin.site.register(frequencia)
admin.site.register(disciplina)
admin.site.register(professores)
admin.site.register(curso)
admin.site.register(coordenador)
# Register your models here.
