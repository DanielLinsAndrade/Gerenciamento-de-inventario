from django.test import TestCase
<<<<<<< HEAD

# Create your tests here.
=======
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient
from django.contrib.auth.models import User


from .models import Funcionario, Category

# Create your tests here.

class ItemTesteCase(TestCase):

    def setUp(self):

        self.category = Category.objects.create(name="Eletrônicos")

        self.novo_item = Funcionario.objects.create(
            name="Iphone",
            price="15000.00",
            description="celular",
            category=self.category
        )

        self.new_user = User.objects.create_user(username="admin", password="adminadmin")
        self.new_user.is_staff = True
        self.new_user.is_superuser = True
        self.new_user.save()
        self.token = Token.objects.create(user=self.new_user)
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token.key}')

    def test_cadastrar_item(self):
        url = "http://localhost:8000/items/"
        data = {"name": "Iphone", "price": "15000.00", "description": "celular caro", "category": 1}

        try:
            response = self.client.post(url, data)
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)
            self.assertTrue(Funcionario.objects.filter(name="Iphone", price="15000.00").exists())
        except ValueError:
            response = self.client.post(url, data)
            self.assertEqual(response.status_code, status.HTTP_409_CONFLICT)

    def test_listar_item(self):
        url = "http://localhost:8000/items/"

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(Funcionario.objects.filter(name="Iphone", price="15000.00").exists())

    def test_atualizar_item(self):
        url = f"http://localhost:8000/items/{self.novo_item.id}/"
        data = {"name": "Iphone", "price": "150.00", "description": "celular barato", "category": 1}

        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(Funcionario.objects.filter(name="Iphone", price="150.00").exists())

    def test_atualizar_parcialmente_item(self):
        url = f"http://localhost:8000/items/{self.novo_item.id}/"
        data = {"price": "200.00", "description": "celular barato"}

        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(Funcionario.objects.filter(name="Iphone", price="200.00").exists())

    def test_deletar_item(self):
        url = f"http://localhost:8000/items/{self.novo_item.id}/"

        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Funcionario.objects.filter(name="Iphone", price="200.00").exists())
>>>>>>> ce1a5a5 (test: Adicionando testes aos itens e usuários)
