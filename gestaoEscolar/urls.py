from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AlunoViewSet, MatriculaViewSet, TurmaViewSet

router = DefaultRouter()
router.register(r'aluno', AlunoViewSet)
router.register(r'matricula', MatriculaViewSet)
router.register(r'turma', TurmaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]