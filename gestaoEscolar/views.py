from rest_framework.viewsets import ModelViewSet
from .models import aluno, matricula, turma, professores, curso, coordenador
from .serializers import AlunoSerializer, MatriculaSerializer, TurmaSerializer, ProfessoresSerializer, CursoSerializer, CoordenadorSerializer

class AlunoViewSet(ModelViewSet):
    queryset = aluno.objects.all()
    serializer_class = AlunoSerializer

class MatriculaViewSet(ModelViewSet):
    queryset = matricula.objects.all()
    serializer_class =  MatriculaSerializer

class TurmaViewSet(ModelViewSet):
    queryset = turma.objects.all()
    serializer_class = TurmaSerializer

class ProfessoresViewSet(ModelViewSet):
    queryset = professores.objects.all()
    serializer_class = ProfessoresSerializer

class CursoViewSet(ModelViewSet):
    queryset = curso.objects.all()
    serializer_class = CursoSerializer

class CoodenadorViewSet(ModelViewSet):
    queryset = coordenador.objects.all()
    serializer_class = CoordenadorSerializer

