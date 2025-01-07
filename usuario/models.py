"""
Modelo Funcionario e UserProfileExample.

Imports:
    from django.db: Ferramentas de banco de dados do Django.
    from django.contrib.auth.models: Modelo User para associação.
"""
from django.db import models
from django.contrib.auth.models import User


class UserProfileExample(models.Model):
    """
    Perfil do usuário estendido com telefone, endereço e data de nascimento.
    """
    phone_number = models.CharField(max_length=12)
    address = models.CharField(max_length=150)
    birth_date = models.DateField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        """
        Configurações de exibição no admin.
        """
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"


class Funcionario(models.Model):
    """
    Representa um funcionário com nome, função e status de gerente.
    """
    nome = models.CharField(max_length=140)
    funcao = models.CharField(max_length=140)
    isGerente = models.BooleanField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        """
        Retorna o nome do funcionário.
        """
        return str(self.nome)

    class Meta:
        """
        Configurações de exibição no admin.
        """
        verbose_name = "Funcionario"
        verbose_name_plural = "Funcionarios"
