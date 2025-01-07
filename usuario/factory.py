import random
from faker import Faker
from django.contrib.auth.models import User
from .models import Funcionario

fake = Faker('pt_BR')

class FuncionarioFactory:

    def create_user(self):
        """Cria e retorna um usuário"""
        new_user = User.objects.create_user(
            username=fake.user_name(),
            password=fake.password()
        )
        return new_user

    def create(self):
        """Cria e retorna um funcionário"""
        novo_funcionario = Funcionario.objects.create(
            nome=fake.name(),
            funcao=fake.job(),
            isGerente=fake.boolean(),
            user=self.create_user()
        )
        return novo_funcionario

    def create_multiple(self, num):
        """Cria múltiplos funcionários"""
        return [self.create() for _ in range(num)]

    def create_batch(self, num):
        """Cria e retorna múltiplos funcionários"""
        return self.create_multiple(num)
