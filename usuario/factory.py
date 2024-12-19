import random
from faker import Faker
from django.contrib.auth.models import User
from .models import Funcionario
from faker import Faker
import random

fake = Faker('pt_BR')


class FuncionarioFactory:

    def create_user(self):
        """
        Cria um novo usuário no modelo User do Django.
        """
        new_user = User.objects.create_user(
            username=fake.user_name(),
            password=fake.password()
        )
        return new_user

    def create(self, is_gerente=False):
        """
        Cria um novo funcionário e associa um usuário do Django.

        Args:
            is_gerente (bool): Define se o funcionário será gerente.

        Returns:
            Funcionario: Um objeto do modelo Funcionario.
        """
        novo_funcionario = Funcionario.objects.create(
            nome=fake.name(),
            funcao=fake.job(),
            isGerente=is_gerente,
            user=self.create_user()
        )
        return novo_funcionario

    def create_multiple(self, num, gerente_ratio=0.2):
        """
        Cria múltiplos funcionários.

        Args:
            num (int): Número de funcionários a serem criados.
            gerente_ratio (float): Proporção de gerentes criados. Ex: 0.2 (20%).

        Returns:
            list[Funcionario]: Uma lista de objetos Funcionario criados.
        """
        funcionarios = []
        for _ in range(num):
            is_gerente = random.random() < gerente_ratio
            funcionarios.append(self.create(is_gerente=is_gerente))
        return funcionarios
