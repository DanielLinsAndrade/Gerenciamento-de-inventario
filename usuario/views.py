from django.shortcuts import render
from rest_framework import viewsets
from .serializers import FuncionarioSerializer
from usuario.models import Funcionario


class UserViewSet(viewsets.ModelViewSet):
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer