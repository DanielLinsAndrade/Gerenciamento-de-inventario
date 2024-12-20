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
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from .serializers import FuncionarioCreateSerializer
from .serializers import FuncionarioSerializer, UserProfileExampleSerializer

from .models import Funcionario, UserProfileExample


class UserProfileExampleViewSet(ModelViewSet):
    """
    ViewSet da API para o modelo UserProfileExample.

    Permite operações `GET` e `PUT` para dados de perfil de usuário.

    Atributos:
        serializer_class: Classe de serialização para UserProfileExample.
        permission_classes: Permissões, permitindo acesso irrestrito.
        queryset: Todos os objetos UserProfileExample.
        http_method_names: Métodos HTTP permitidos, 'GET' e 'PUT'.
    """
    serializer_class = UserProfileExampleSerializer
    permission_classes = [IsAuthenticated]
    queryset = UserProfileExample.objects.all()
    http_method_names = ['get', 'put']


class FuncionarioViewSet(ModelViewSet):
    """
    ViewSet da API para o modelo Funcionario.

    Fornece operações CRUD e customiza o método `create` para incluir criação
    de usuário e atribuição a grupo.

    Atributos:
        serializer_class: Classe de serialização para Funcionario.
        permission_classes: Permissões, permitindo acesso irrestrito.
        queryset: Todos os objetos Funcionario.

    Métodos:
        create: Cria um novo funcionário e usuário, atribuindo ao grupo
        "Gerentes".
    """
    serializer_class = FuncionarioSerializer
    permission_classes = [IsAuthenticated]
    queryset = Funcionario.objects.all()

    def create(self, request):
        """
        Cria um novo registro de Funcionario e associa um usuário ao grupo de
        gerentes, se necessário. Este método:
        - Valida os dados enviados pelo cliente utilizando o
        `FuncionarioCreateSerializer`.
        - Garante que o nome de usuário (`username`) seja único, adicionando um
        número incremental caso já exista.
        - Cria um novo usuário com o nome de usuário e senha fornecidos.
        - Adiciona o novo usuário ao grupo "Gerentes", se necessário.
        - Cria um novo registro de `Funcionario` associado ao usuário criado.
        - Retorna os dados do funcionário criado e uma mensagem de sucesso.

        Em caso de erro, retorna uma mensagem detalhada e status HTTP
        apropriado.
        """
        try:
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

        except ValueError as e:
            # Retorna uma mensagem genérica de erro para o cliente
            return Response(
                {"error": "Ocorreu um erro ao criar o funcionário.",
                    "details": str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )
