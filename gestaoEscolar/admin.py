from django.contrib import admin
from .models import aluno, matricula, turma, professores, curso


admin.site.register(aluno)
admin.site.register(matricula)
admin.site.register(turma)
admin.site.register(professores)
admin.site.register(curso)
# Register your models here.
