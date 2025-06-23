from rest_framework.serializers import ModelSerializer
from .models import aluno, matricula, turma, nota, frequencia, disciplina, professores, curso, coordenador

class AlunoSerializer(ModelSerializer):
    class Meta:
        model = aluno
        fields = '__all__'

class MatriculaSerializer(ModelSerializer):
    class Meta:
        model = matricula
        fields = '__all__'

class TurmaSerializer(ModelSerializer):
    class Meta:
        model = turma
        fields = '__all__'

class NotaSerializer(ModelSerializer):
    class Meta:
        model = nota
        fields = '__all__'

class FrequenciaSerializer(ModelSerializer):
    class Meta:
        model = frequencia
        fields = '__all__'

class DisciplinaSerializer(ModelSerializer):
    class Meta:
        model = disciplina
        fields = '__all__'

class ProfessoresSerializer(ModelSerializer):
    class Meta:
        model = professores
        fields = '__all__'

class CursoSerializer(ModelSerializer):
    class Meta:
        model = curso
        fields =  '__all__'

class CoordenadorSerializer(ModelSerializer):
    class Meta:
        model = coordenador
        fields = '__all__'