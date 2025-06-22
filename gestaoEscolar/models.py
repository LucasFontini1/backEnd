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
    
class turma(models.Model):
    nome = models.CharField(max_length=100, blank=True, null=True)
    anoRegistro = models.IntegerField(blank=True, null=True)
    periodo = models.CharField(max_length=20, choices=[('manhã', 'Manhã'), ('tarde', 'Tarde'), ('noite', 'Noite')], blank=True, null=True)

    def __str__(self):
        return f"{self.nome} - {self.anoRegistro} - {self.periodo}"
    
class professores(models.Model):
    cpf = models.CharField(max_length=11, primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(max_length=254, blank=True, null=True)
    data_nascimento = models.DateField(blank=True, null=True)
    endereco = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.nome}"

class curso(models.Model):
    codigo_curso = models.CharField(max_length=50, primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    modalidade = models.CharField(max_length=20, choices=[('semipresencial', 'Semipresencial'), ('online', 'Online'), ('presencial', 'Presencial')])
    carga_horaria = models.IntegerField(null=True)

    def __str__(self):
        return f"{self.nome} - {self.modalidade} - {self.carga_horaria} horas"
    
class coordenador(models.Model):
    cpf = models.CharField(max_length=11, primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(max_length=254, blank=True, null=True)
    data_nascimento = models.DateField(blank=True, null=True)
    endereco = models.CharField(max_length=255, blank=True, null=True)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    curso = models.ForeignKey('Curso', on_delete=models.PROTECT, blank=True, null=True)

    def __str__(self):
        return f"{self.nome} - {self.curso.nome}"
    