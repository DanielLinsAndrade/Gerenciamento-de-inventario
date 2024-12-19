"""
Módulo que define o modelo Funcionario.

Imports:
    from django.db: Importa as ferramentas de banco de dados do Django.
    from django.contrib.auth.models: Importa o modelo User para associar
    ao Funcionario.
"""
from django.db import models
from django.contrib.auth.models import User


class UserProfileExample(models.Model):

    phone_number = models.CharField(max_length=12)
    address = models.CharField(max_length=150)
    birth_date = models.DateField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"

class Funcionario(models.Model):
    """
    Modelo que representa um funcionário.

    Atributos:
        nome (str): O nome do funcionário.
        funcao (str): A função exercida pelo funcionário.
        isGerente (bool): Indica se o funcionário é um gerente.
        user (User): Associação um-para-um com o modelo User do Django.
    """
    nome = models.CharField(max_length=140)
    funcao = models.CharField(max_length=140)
    isGerente = models.BooleanField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        """
        Retorna o nome do funcionário como uma string.
        """
        return str(self.nome)

    class Meta:
        """
        Metadados para o modelo Funcionario.

        Atributos:
            verbose_name (str): Nome singular do modelo.
            verbose_name_plural (str): Nome plural do modelo.
        """
        verbose_name = "Funcionario"
        verbose_name_plural = "Funcionarios"
