from rest_framework import serializers
<<<<<<< HEAD
from .models import Category, Item
=======
from .models import Category, Funcionario
>>>>>>> ce1a5a5 (test: Adicionando testes aos itens e usuários)

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
<<<<<<< HEAD
        model = Item
=======
        model = Funcionario
>>>>>>> ce1a5a5 (test: Adicionando testes aos itens e usuários)
        fields = '__all__'