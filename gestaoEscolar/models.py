from django.db import models

class aluno(models.Model):
    cpf = models.CharField(max_length=14, primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    data_nascimento = models.DateField(blank=True, null=True)
    email = models.EmailField(max_length=254, blank=True, null=True)
    endereco = models.CharField(max_length=255, blank=True, null=True)
    matricula = models.ForeignKey('matricula', on_delete=models.CASCADE, blank=True, null=True)
    turma = models.ForeignKey('turma', on_delete=models.PROTECT, blank=True, null=True)
    
    def __str__(self):
        return f"{self.nome} "
    
class matricula(models.Model):
    data_matricula = models.DateField(auto_now_add=True, blank=True, null=True)
    status = models.CharField(max_length=20, choices=[('ativo', 'Ativo'), ('inativo', 'Inativo')], default='ativo', blank=True, null=True)
    numero = models.CharField(max_length=20, unique=True, blank=True, null=True)


    def __str__(self):
        return f"{self.numero} - {self.status}"
    
class turma(models.Model):
    nome = models.CharField(max_length=100, blank=True, null=True)
    anoRegistro = models.IntegerField(blank=True, null=True)
    periodo = models.CharField(max_length=20, choices=[('manhã', 'Manhã'), ('tarde', 'Tarde'), ('noite', 'Noite'),('integral', 'Integral')], blank=True, null=True)

    def __str__(self):
        return f"{self.nome} - {self.anoRegistro} - {self.periodo}"

class nota(models.Model):
    nota_total = models.CharField(max_length=4)
    nota_aluno = models.CharField(max_length=4)
    aluno = models.ForeignKey('aluno', on_delete=models.PROTECT, blank=True, null=True)

    def __str__(self):
        return f"{self.aluno} - {self.nota_aluno}/{self.nota_total}"

class frequencia(models.Model):
    data_presenca = models.DateField(verbose_name='Data:')
    presenca_aluno = models.CharField(max_length=15, choices={('falta', 'Falta'), ('presente', 'Presente'), ('justificada', 'Justificada')})
    aluno = models.ForeignKey('aluno', on_delete=models.PROTECT, blank=True, null=True)

    def __str__(self):
        return f"{self.aluno} - {self.data_presenca}, {self.presenca_aluno}"

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
    carga_horaria = models.IntegerField(max_length=5, null=True)


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


    