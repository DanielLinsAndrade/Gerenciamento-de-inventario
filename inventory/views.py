from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import APIException

from .models import Category, Funcionario
from .serializers import CategorySerializer, ItemSerializer
from .services import criar_categoria, criar_item, filtrar_itens_por_categoria


class CategoryViewSet(viewsets.ModelViewSet):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]

    def create(self, request):
        try:
            # Usa o serviço para criar a categoria
            data = criar_categoria(request.data, self.get_serializer_class())
            return Response(data, status=status.HTTP_201_CREATED)
        except APIException as e:
            return Response(
                {"detail": str(e)},
                status=getattr(e, 'status_code', status.HTTP_400_BAD_REQUEST)
            )


class ItemViewSet(viewsets.ModelViewSet):

    queryset = Funcionario.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request):
        try:
            # Usa o serviço para criar o item
            data = criar_item(request.data, self.get_serializer_class())
            return Response(data, status=status.HTTP_201_CREATED)
        except APIException as e:
            return Response(
                {"detail": str(e)},
                status=getattr(e, 'status_code', status.HTTP_400_BAD_REQUEST)
            )

    @action(detail=False, methods=['get'])
    def filter_by_category(self, request):
        category_name = request.query_params.get('category', None)
        try:
            # Usa o serviço para filtrar itens por categoria
            data = filtrar_itens_por_categoria(category_name, self.get_serializer_class())
            return Response(data, status=status.HTTP_200_OK)
        except APIException as e:
            return Response(
                {"error": str(e)},
                status=getattr(e, 'status_code', status.HTTP_400_BAD_REQUEST)
            )
        except ValueError as e:
            return Response(
                {"error": "Ocorreu um erro inesperado.", "details": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
