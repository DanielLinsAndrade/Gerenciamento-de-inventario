"""
Este módulo define ViewSets para gerenciar recursos
relacionados a categorias e itens.

Ele inclui classes para fornecer as operações padrão
de CRUD (Create, Read, Update, Delete)
para as models Category e Item, além de uma ação customizada
para filtrar itens por categoria.

Classes:
    - CategoryViewSet: Gerencia as operações
    relacionadas a categorias.
    - ItemViewSet: Gerencia as operações relacionadas a itens,
    incluindo filtro por categoria.

Dependências:
    - Django REST Framework: Fornece as bases para a criação de APIs RESTful.
    - Models Category e Item: Representam as entidades principais do domínio.
    - Serializers CategorySerializer e ItemSerializer: Serializadores para
    validação e transformação dos dados.
"""

<<<<<<< HEAD
# from django.shortcuts import render  # noqa: F401
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import Category, Item
=======
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Category, Funcionario
>>>>>>> ce1a5a5 (test: Adicionando testes aos itens e usuários)
from .serializers import CategorySerializer, ItemSerializer

# Nota: Os comentários "# noqa: E1101" são usados para informar
# ao Pylint que as propriedades e membros
# (como 'objects' e 'DoesNotExist') de Category e Item são gerados
# dinamicamente pelo Django ORM.
# Esses membros existem em tempo de execução, mas não são detectados pela
# análise estática do Pylint.


class CategoryViewSet(viewsets.ModelViewSet):
    """
    ViewSet para operações CRUD na model Category.

    Este ViewSet fornece as ações padrão para listar, criar, atualizar,
    recuperar e deletar instâncias de Category.
    """
<<<<<<< HEAD
    permission_classes = [IsAuthenticated]
=======
>>>>>>> ce1a5a5 (test: Adicionando testes aos itens e usuários)
    queryset = Category.objects.all()  # noqa: E1101
    serializer_class = CategorySerializer


class ItemViewSet(viewsets.ModelViewSet):
    """
    ViewSet para operações CRUD na model Item.

    Este ViewSet fornece as ações padrão para listar, criar, atualizar,
    recuperar e deletar instâncias de Item. Também inclui uma ação customizada
    para filtrar itens por categoria.
    """
<<<<<<< HEAD
    queryset = Item.objects.all()  # noqa: E1101
=======
    queryset = Funcionario.objects.all()  # noqa: E1101
>>>>>>> ce1a5a5 (test: Adicionando testes aos itens e usuários)
    serializer_class = ItemSerializer

    @action(detail=False, methods=['get'])
    def filter_by_category(self, request):
        """
        Filtra os itens por uma categoria específica.

        Espera-se que o parâmetro de consulta "category" seja fornecido na
        requisição. Retorna os itens pertencentes à categoria especificada.

        Parâmetros:
            request (Request): O objeto de requisição HTTP.

        Retorna:
            Response: Os itens filtrados ou uma mensagem de erro apropriada.
        """
        category_name = request.query_params.get('category', None)

        if not category_name:
            return Response(
                {"error": "O parâmetro 'category' é obrigatório."},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            category = Category.objects.get(name=category_name)  # noqa: E1101
            items = category.items.all()
            serializer = self.get_serializer(items, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Category.DoesNotExist:  # noqa: E1101
            return Response(
                {"error": f"Categoria '{category_name}' não encontrada."},
                status=status.HTTP_404_NOT_FOUND
            )
        except Category.MultipleObjectsReturned:
            return Response(
                {"error": f"Várias categorias'{category_name}' encontradas."},
                status=status.HTTP_400_BAD_REQUEST
            )
        except ValueError as e:
            return Response(
                {"error": "Ocorreu um erro inesperado.", "details": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
