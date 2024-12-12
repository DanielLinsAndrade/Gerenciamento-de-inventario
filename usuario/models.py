from django.db import models
from django.contrib.auth.models import User

class Funcionario(models.Model):

    nome = models.CharField(max_length=140)
    funcao = models.CharField(max_length=140)
    isGerente = models.BooleanField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = "Funcionario"
        verbose_name_plural = "Funcionarios"