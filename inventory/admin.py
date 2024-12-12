from django.contrib import admin
from .models import Category, Item

# Registrando os modelos no admin
admin.site.register(Category)
admin.site.register(Item)