"""
Modelos Django para representar uma categoria e itens dentro dessa categoria.

Classes:
    Category: Representa uma categoria de itens com nome e descrição.
    Item: Representa um item pertencente a uma categoria, contendo nome,
    quantidade, preço e descrição.

Métodos:
    __str__: Retorna a representação em string do nome da categoria ou do item.
"""

from django.db import models


class Category(models.Model):
    """
    Representa uma categoria de itens.
    """
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        """
        Retorna o nome da categoria como string.
        """
        return str(self.name)


class Item(models.Model):

class Funcionario(models.Model):
    """
    Representa um item dentro de uma categoria, com quantidade,
    preço e descrição.
    """
    name = models.CharField(max_length=100)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='items'
    )
    quantity = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=100)

    def __str__(self):
        """
        Retorna o nome do item como string.
        """
        return str(self.name)
