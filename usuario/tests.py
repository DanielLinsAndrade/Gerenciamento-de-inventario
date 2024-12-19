from django.test import TestCase

from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient
from django.contrib.auth.models import User, Group


from .models import Funcionario

# Create your tests here.

class FuncionarioTesteCase(TestCase):

    def setUp(self):

        self.new_user = User.objects.create_user(username="admin", password="adminadmin") # NOSONAR
        self.new_user.is_staff = True
        self.new_user.is_superuser = True
        gerente_group, _ = Group.objects.get_or_create(name="Gerente")
        self.new_user.groups.add(gerente_group)
        self.new_user.save()
        self.token = Token.objects.create(user=self.new_user)
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token.key}')

        self.novo_funcionario = Funcionario.objects.create(
            nome="Jão",
            funcao="Gerente Financeiro",
            isGerente=True,
		    user= self.new_user
        )

    def test_cadastrar_funcionario(self):
        url = "http://localhost:8000/gerentes/"
        data = {"nome": "Jão", "funcao": "Gerente Financeiro",
                "isGerente": True, "user": self.new_user.id}

        response = self.client.post(url, data)
        if response.status_code == status.HTTP_201_CREATED:
            self.assertTrue(Funcionario.objects.filter(nome="Jão", funcao="Gerente Financeiro").exists())
        else:
            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


    def test_listar_funcionario(self):
        url = "http://localhost:8000/gerentes/"

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(Funcionario.objects.filter(nome="Jão", funcao="Gerente Financeiro").exists())

    def test_atualizar_funcionario(self):
        url = f"http://localhost:8000/gerentes/{self.novo_funcionario.id}/"
        data = {"nome": "Daniel", "funcao": "programador",
                "isGerente": True, "user": self.new_user.id}

        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(Funcionario.objects.filter(nome="Daniel", funcao="programador").exists())

    def test_atualizar_parcialmente_funcionario(self):
        url = f"http://localhost:8000/gerentes/{self.novo_funcionario.id}/"
        data = {"nome": "Gerson", "funcao": "front"}

        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(Funcionario.objects.filter(nome="Gerson", funcao="front").exists())

    def test_deletar_funcionario(self):
        url = f"http://localhost:8000/gerentes/{self.novo_funcionario.id}/"

        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Funcionario.objects.filter(nome="Daniel", funcao="tester").exists())
