from django.contrib import admin

from .models import Category, Funcionario

# Registrando os modelos no admin
admin.site.register(Category)
admin.site.register(Funcionario)
