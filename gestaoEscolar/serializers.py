from rest_framework.serializers import ModelSerializer
from .models import aluno, matricula

class AlunoSerializer(ModelSerializer):
    class Meta:
        model = aluno
        fields = '__all__'

class MatriculaSerializer(ModelSerializer):
    class Meta:
        model = matricula
        fields = '__all__'