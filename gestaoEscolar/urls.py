from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AlunoViewSet, MatriculaViewSet, TurmaViewSet, ProfessoresViewSet

router = DefaultRouter()
router.register(r'aluno', AlunoViewSet)
router.register(r'matricula', MatriculaViewSet)
router.register(r'turma', TurmaViewSet)
router.register(r'professores', ProfessoresViewSet)

urlpatterns = [
    path('', include(router.urls)),
]