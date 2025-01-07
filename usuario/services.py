from django.contrib.auth.models import User, Group
from .models import Funcionario
from .serializers import FuncionarioSerializer
from .serializers import FuncionarioCreateSerializer


def criar_funcionario(data):
    """
    Cria um novo funcionário, associando-o a um usuário e grupo específico.
    """
    # Valida os dados do serializer
    serializer = FuncionarioCreateSerializer(data=data)
    serializer.is_valid(raise_exception=True)

    # Gera o username único
    username = serializer.validated_data['login']
    original_username = username
    count = 1
    while User.objects.filter(username=username).exists():
        username = f"{original_username}{count}"
        count += 1

    # Cria o usuário
    novo_user = User.objects.create_user(
        username=username,
        password=serializer.validated_data['senha'],
    )

    # Associa o grupo
    grupo_gerentes, _ = Group.objects.get_or_create(name="Gerentes")
    novo_user.groups.add(grupo_gerentes)

    # Define se o funcionário é gerente
    is_gerente = serializer.validated_data.get('isGerente', False)

    # Cria o funcionário
    novo_gerente = Funcionario.objects.create(
        nome=serializer.validated_data['nome'],
        funcao=serializer.validated_data['funcao'],
        isGerente=is_gerente,
        user=novo_user
    )

    # Serializa os dados de saída
    serializer_saida = FuncionarioSerializer(novo_gerente)
    return serializer_saida.data
