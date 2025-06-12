from django.db import models

class aluno(models.Model):
    cpf = models.CharField(max_length=11, primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    data_nascimento = models.DateField(blank=True, null=True)
    email = models.EmailField(max_length=254, blank=True, null=True)
    endereco = models.CharField(max_length=255, blank=True, null=True)
    matricula = models.ForeignKey('matricula', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f"{self.nome} "
    
class matricula(models.Model):
    data_matricula = models.DateField(auto_now_add=True, blank=True, null=True)
    status = models.CharField(max_length=20, choices=[('ativo', 'Ativo'), ('inativo', 'Inativo')], default='ativo', blank=True, null=True)
    numero = models.CharField(max_length=20, unique=True, blank=True, null=True)


    def __str__(self):
        return f"{self.aluno.nome} - {self.numero} - {self.status}"