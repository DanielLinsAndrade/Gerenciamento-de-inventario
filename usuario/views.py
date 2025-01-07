"""
Imports necessários para views, permissões, respostas, modelos e serviços.
"""
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from .models import Funcionario, UserProfileExample
from .serializers import FuncionarioSerializer, UserProfileExampleSerializer
from .services import criar_funcionario  # Importa o serviço


class UserProfileExampleViewSet(ModelViewSet):
    """
    Gerencia perfis de usuário. Apenas GET e PUT são permitidos.
    """
    serializer_class = UserProfileExampleSerializer
    permission_classes = [IsAuthenticated]
    queryset = UserProfileExample.objects.all()
    http_method_names = ['get', 'put']


class FuncionarioViewSet(ModelViewSet):
    """
    Gerencia funcionários e cria novos usando um serviço.
    """
    serializer_class = FuncionarioSerializer
    permission_classes = [IsAuthenticated]
    queryset = Funcionario.objects.all()

    def create(self, request):
        """
        Cria um funcionário usando dados enviados na requisição.
        """
        try:
            data = criar_funcionario(request.data)
            return Response(
                {"Info": "Cadastro realizado!", "data": data},
                status=status.HTTP_201_CREATED
            )
        except ValueError as e:
            return Response(
                {"error": "Erro ao criar funcionário.", "details": str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )
