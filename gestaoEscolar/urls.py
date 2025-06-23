from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AlunoViewSet, MatriculaViewSet

router = DefaultRouter()
router.register(r'aluno', AlunoViewSet)
router.register(r'matricula', MatriculaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]