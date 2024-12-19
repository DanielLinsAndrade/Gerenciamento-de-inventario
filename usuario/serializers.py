from rest_framework import serializers
from .models import Funcionario, UserProfileExample
from django.contrib.auth.models import User

class UserProfileExampleSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfileExample
        fields = ['id', 'address', 'phone_number', 'birth_date', 'user']

class FuncionarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Funcionario
        fields = '__all__'
        
class FuncionarioCreateSerializer(serializers.Serializer):
    nome = serializers.CharField(max_length=140)
    funcao = serializers.CharField(max_length=140)
    isGerente = serializers.BooleanField()
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    login = serializers.CharField(max_length=150)
    senha = serializers.CharField(write_only=True)
