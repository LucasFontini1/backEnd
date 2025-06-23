from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AlunoViewSet, MatriculaViewSet, TurmaViewSet, ProfessoresViewSet, CursoViewSet, CoodenadorViewSet

router = DefaultRouter()
router.register(r'aluno', AlunoViewSet)
router.register(r'matricula', MatriculaViewSet)
router.register(r'turma', TurmaViewSet)
router.register(r'professores', ProfessoresViewSet)
router.register(r'curso', CursoViewSet)
router.register(r'coodenador', CoodenadorViewSet)

urlpatterns = [
    path('', include(router.urls)),
]