from rest_framework.viewsets import ModelViewSet
from .models import aluno
from .serializers import AlunoSerializer

class AlunoViewSet(ModelViewSet):
    queryset = aluno.objects.all()
    serializer_class = AlunoSerializer

