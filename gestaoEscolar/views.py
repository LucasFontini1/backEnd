from rest_framework.viewsets import ModelViewSet
from .models import aluno, matricula
from .serializers import AlunoSerializer, MatriculaSerializer

class AlunoViewSet(ModelViewSet):
    queryset = aluno.objects.all()
    serializer_class = AlunoSerializer

class MatriculaViewSet(ModelViewSet):
    queryset = matricula.objects.all()
    serializer_class =  MatriculaSerializer

