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
    """
    Modelo que representa o perfil de um usuário.

    Este modelo estende o modelo padrão do Django `User` com informações
    adicionais sobre o perfil, como número de telefone, endereço e data de
    nascimento.

    Atributos:
        phone_number (str): Número de telefone do usuário, com até 12
            caracteres.
        address (str): Endereço do usuário, com até 150 caracteres.
        birth_date (date): Data de nascimento do usuário.
        user (User): Associação um-para-um com o modelo `User` do Django.

    Metadados:
        verbose_name (str): Nome legível para uma instância singular deste
            modelo.
        verbose_name_plural (str): Nome legível para o plural deste modelo.
    """
    phone_number = models.CharField(max_length=12)
    address = models.CharField(max_length=150)
    birth_date = models.DateField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        """
        Configurações de exibição do modelo.

        verbose_name: Nome singular exibido no admin.
        verbose_name_plural: Nome plural exibido no admin.
        """
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
