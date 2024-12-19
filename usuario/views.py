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
from django.contrib.auth.models import User, Group
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import FuncionarioCreateSerializer, FuncionarioSerializer, UserProfileExampleSerializer
from usuario.api.permissions import IsGerente

from .models import Funcionario, UserProfileExample


class UserProfileExampleViewSet(ModelViewSet):
    serializer_class = UserProfileExampleSerializer
    permission_classes = [AllowAny]
    queryset = UserProfileExample.objects.all()
    http_method_names = ['get', 'put']

class FuncionarioViewSet(ModelViewSet):
    serializer_class = FuncionarioSerializer
    permission_classes = [AllowAny]
    queryset = Funcionario.objects.all()

    def create(self, request):
        serializer = FuncionarioCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        username = serializer.validated_data['login']
        original_username = username
        count = 1
        while User.objects.filter(username=username).exists():
            username = f"{original_username}{count}"
            count += 1

        novo_user = User.objects.create_user(
            username=username,
            password=serializer.validated_data['senha'],
        )

        grupo_gerentes, _ = Group.objects.get_or_create(name="Gerentes")
        novo_user.groups.add(grupo_gerentes)

        is_gerente = serializer.validated_data.get('isGerente', False)
        
        novo_gerente = Funcionario.objects.create(
            nome=serializer.validated_data['nome'],
            funcao=serializer.validated_data['funcao'],
            isGerente=is_gerente,
            user=novo_user
        )

        serializer_saida = FuncionarioSerializer(novo_gerente)
        return Response({"Info": "Cadastro realizado!",
                         "data": serializer_saida.data},
                        status=status.HTTP_201_CREATED)
