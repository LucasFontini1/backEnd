from rest_framework.viewsets import ModelViewSet
from .models import aluno, matricula, turma, nota, frequencia, professores, curso, coordenador 
from .serializers import AlunoSerializer, MatriculaSerializer, TurmaSerializer, NotaSerializer, FrequenciaSerializer, ProfessoresSerializer, CursoSerializer, CoordenadorSerializer

class AlunoViewSet(ModelViewSet):
    queryset = aluno.objects.all()
    serializer_class = AlunoSerializer

class MatriculaViewSet(ModelViewSet):
    queryset = matricula.objects.all()
    serializer_class =  MatriculaSerializer

class TurmaViewSet(ModelViewSet):
    queryset = turma.objects.all()
    serializer_class = TurmaSerializer

class NotaViewSet(ModelViewSet):
    queryset = nota.objects.all()
    serializer_class = NotaSerializer

class FrequenciaViewSet(ModelViewSet):
    queryset = frequencia.objects.all()
    serializer_class = FrequenciaSerializer

class ProfessoresViewSet(ModelViewSet):
    queryset = professores.objects.all()
    serializer_class = ProfessoresSerializer

class CursoViewSet(ModelViewSet):
    queryset = curso.objects.all()
    serializer_class = CursoSerializer

class CoodenadorViewSet(ModelViewSet):
    queryset = coordenador.objects.all()
    serializer_class = CoordenadorSerializer

