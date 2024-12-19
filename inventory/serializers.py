from rest_framework import serializers

from .models import Category, Funcionario


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Funcionario
        fields = '__all__'
