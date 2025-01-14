"""
Importa as ferramentas do Django REST Framework necessárias para as views.
"""
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import APIException

from .models import Category, Funcionario
from .serializers import CategorySerializer, ItemSerializer
from .services import criar_categoria, criar_item, filtrar_itens_por_categoria


class CategoryViewSet(viewsets.ModelViewSet):
    """
    Gerencia as categorias de itens.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]

    def create(self, request):
        """
        Cria uma nova categoria.
        """
        try:
            data = criar_categoria(request.data, self.get_serializer_class())
            return Response(data, status=status.HTTP_201_CREATED)
        except APIException as e:
            return Response(
                {"detail": str(e)},
                status=getattr(e, 'status_code', status.HTTP_400_BAD_REQUEST)
            )


class ItemViewSet(viewsets.ModelViewSet):
    """
    Gerencia os itens (funcionários).
    """
    queryset = Funcionario.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request):
        """
        Cria um novo item.
        """
        try:
            data = criar_item(request.data, self.get_serializer_class())
            return Response(data, status=status.HTTP_201_CREATED)
        except APIException as e:
            return Response(
                {"detail": str(e)},
                status=getattr(e, 'status_code', status.HTTP_400_BAD_REQUEST)
            )

    @action(detail=False, methods=['get'])
    def filter_by_category(self, request):
        """
        Filtra itens pela categoria.
        """
        category_name = request.query_params.get('category', None)
        try:
            data = filtrar_itens_por_categoria(category_name, self.get_serializer_class())
            return Response(data, status=status.HTTP_200_OK)
        except APIException as e:
            return Response(
                {"error": str(e)},
                status=getattr(e, 'status_code', status.HTTP_400_BAD_REQUEST)
            )
        except ValueError as e:
            return Response(
                {"error": "Erro inesperado.", "details": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
