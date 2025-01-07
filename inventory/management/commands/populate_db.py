from django.core.management.base import BaseCommand
from inventory.factory import CategoryFactory, FuncionarioFactory


class Command(BaseCommand):
    help = 'Popula o banco de dados com categorias e itens fictícios'

    def handle(self, *args, **kwargs):
        # Criando categorias e itens
        categories = CategoryFactory.create_batch(5)  # Cria 5 categorias
        for category in categories:
            FuncionarioFactory.create_batch(3, category)  # Cria 3 itens para cada categoria

        self.stdout.write(self.style.SUCCESS('Banco de dados populado com sucesso!'))
