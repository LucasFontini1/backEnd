from rest_framework.serializers import ModelSerializer
from .models import aluno

class AlunoSerializer(ModelSerializer):
    class Meta:
        model = aluno
        fields = '__all__'