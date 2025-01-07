"""
Importa os modelos necessários do Django para criação das tabelas.
"""
from django.db import models


class Category(models.Model):
    """
    Categoria de itens com nome e descrição.
    """
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        """
        Retorna o nome da categoria.
        """
        return str(self.name)


class Funcionario(models.Model):
    """
    Item com nome, categoria, quantidade, preço e descrição.
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
        Retorna o nome do item.
        """
        return str(self.name)
