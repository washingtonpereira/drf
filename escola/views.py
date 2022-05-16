from rest_framework import viewsets

from escola.models import Aluno
from escola.serializer import AlunoSerializer


class AlunosViewset(viewsets.ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer
