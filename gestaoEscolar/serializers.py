from rest_framework.serializers import ModelSerializer
from .models import aluno, matricula, turma, professores

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

class ProfessoresSerializer(ModelSerializer):
    class Meta:
        model = professores
        fields = '__all__'