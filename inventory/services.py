from rest_framework.exceptions import APIException
from .models import Category, Funcionario
from .serializers import ItemSerializer, CategorySerializer


def criar_categoria(data, serializer_class):
    """
    Lógica de criação de uma categoria.
    """
    serializer = serializer_class(data=data)
    serializer.is_valid(raise_exception=True)
    categoria = serializer.save()
    return serializer.data


def criar_item(data, serializer_class):
    """
    Lógica de criação de um item.
    """
    serializer = serializer_class(data=data)
    serializer.is_valid(raise_exception=True)
    item = serializer.save()
    return serializer.data


def filtrar_itens_por_categoria(category_name, serializer_class):
    """
    Filtra itens por nome de categoria.
    """
    if not category_name:
        raise ValueError("O parâmetro 'category' é obrigatório.")

    try:
        category = Category.objects.get(name=category_name)
        items = category.items.all()
        serializer = serializer_class(items, many=True)
        return serializer.data
    except Category.DoesNotExist:
        raise APIException(f"Categoria '{category_name}' não encontrada.", code=404)
    except Category.MultipleObjectsReturned:
        raise APIException(f"Várias categorias '{category_name}' encontradas.", code=400)
