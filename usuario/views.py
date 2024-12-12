"""
ViewSet da API que permite operações CRUD no modelo Funcionario.

    Classes:
        UserViewSet: Um viewset que fornece as ações padrão `list`,
        `create`, `retrieve`, `update` e `destroy` para o modelo Funcionario.

    Atributos:
        queryset (QuerySet): O conjunto de consultas contendo todos
        os objetos Funcionario.
        serializer_class (Serializer): A classe do serializador que
        será usada para a validação e deserialização dos dados do Funcionario.
"""

# from django.shortcuts import render # noqa: F401
from rest_framework import viewsets
from usuario.models import Funcionario
from .serializers import FuncionarioSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    ViewSet para realizar operações CRUD no modelo Funcionario.

    Este viewset fornece as seguintes ações padrão:
        - list: Listar todos os objetos Funcionario.
        - create: Criar um novo objeto Funcionario.
        - retrieve: Recuperar um objeto Funcionario específico.
        - update: Atualizar um objeto Funcionario existente.
        - destroy: Excluir um objeto Funcionario.

    Atributos:
        queryset (QuerySet): O conjunto de consultas contendo todos
        os objetos Funcionario.
        serializer_class (Serializer): A classe do serializador usada
        para validar e deserializar os dados do Funcionario.
    """
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer
