from django.core.management.base import BaseCommand
from usuario.factory import FuncionarioFactory


class Command(BaseCommand):

    help = "Popula o banco de dados com dados fictícios"

    def handle(self, *args, **kwargs):

        # Cria funcionários
        FuncionarioFactory().create_batch(10)

        self.stdout.write(self.style.SUCCESS("Banco de dados populado com sucesso!"))
