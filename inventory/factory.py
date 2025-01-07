import random
from faker import Faker
from .models import Category, Funcionario

fake = Faker('pt_BR')

# Lista personalizada de categorias e nomes de itens
category_names = [
    "Eletrônicos", "Vestuário", "Alimentos", "Móveis", "Brinquedos", "Beleza e Cuidados"
]

# Lista de descrições para as categorias
category_descriptions = {
    "Eletrônicos": "Produtos tecnológicos de última geração, incluindo dispositivos móveis, computadores e acessórios.",
    "Vestuário": "Roupas para todas as idades, desde peças casuais até roupas formais.",
    "Alimentos": "Itens alimentícios variados, com opções frescas, congeladas e embaladas.",
    "Móveis": "Móveis para todos os tipos de ambientes, de salas de estar a escritórios e cozinhas.",
    "Brinquedos": "Brinquedos educativos e de entretenimento para crianças de todas as idades.",
    "Beleza e Cuidados": "Produtos de cuidados pessoais, desde cosméticos até equipamentos para cuidados de pele e cabelo."
}

item_names = [
    "Celular", "Notebook", "Camiseta", "Cadeira", "Fone de ouvido", "Abacaxi", "Maçã", "Banana",
    "Manga", "Melancia", "Cadeira de escritório", "Copo", "Chave", "Caneta", "Mouse", "TV", "Geladeira"
]

# Lista de descrições mais plausíveis para os itens
item_descriptions = {
    "Celular": "Smartphone com tela de 6,5 polegadas e câmera de 12MP, ideal para uso diário e entretenimento.",
    "Notebook": "Computador portátil com processador Intel i7, 16GB de RAM e 512GB de SSD.",
    "Camiseta": "Camiseta de algodão, disponível em diversas cores e tamanhos. Confortável para o uso diário.",
    "Cadeira": "Cadeira ergonômica para escritório, com ajuste de altura e apoio lombar.",
    "Fone de ouvido": "Fones de ouvido sem fio, com cancelamento de ruído e bateria de longa duração.",
    "Abacaxi": "Fruta tropical rica em vitamina C, ideal para sucos ou consumo in natura.",
    "Maçã": "Fruta crocante e doce, excelente para lanches rápidos e saudável.",
    "Banana": "Fruta rica em potássio, ideal para um lanche rápido e nutritivo.",
    "Manga": "Fruta doce e suculenta, perfeita para sobremesas e smoothies.",
    "Melancia": "Fruta refrescante e doce, ideal para o verão e picnics.",
    "Cadeira de escritório": "Cadeira confortável para longas horas de trabalho, com regulagem de altura e apoio para os braços.",
    "Copo": "Copo de vidro, ideal para servir bebidas frias ou quentes.",
    "Chave": "Chave de segurança, feita de material resistente e durável.",
    "Caneta": "Caneta esferográfica com tinta preta, ideal para escrita diária.",
    "Mouse": "Mouse sem fio com alta precisão, confortável para uso prolongado.",
    "TV": "Televisor LED 4K com tela de 50 polegadas e tecnologia Smart TV.",
    "Geladeira": "Geladeira com capacidade de 300 litros, com função de congelamento rápido."
}

# Factory para criar Categorias
class CategoryFactory:

    @staticmethod
    def create():
        category_name = fake.random_element(category_names)
        category = Category.objects.create(
            name=category_name,
            description=category_descriptions.get(category_name, fake.text(max_nb_chars=200))  # Descrição mais realista ou genérica
        )
        return category

    @staticmethod
    def create_batch(num):
        return [CategoryFactory.create() for _ in range(num)]


# Factory para criar Itens (Funcionários)
class FuncionarioFactory:
    
    @staticmethod
    def create(category=None):
        if not category:
            category = CategoryFactory.create()

        # Escolhe um nome de item da lista
        item_name = fake.random_element(item_names)
        
        funcionario = Funcionario.objects.create(
            name=item_name,  # Nome do item
            category=category,
            quantity=random.randint(1, 100),
            price=random.randint(50, 1000),  # Preço aleatório entre 50 e 1000
            description=item_descriptions.get(item_name, fake.text(max_nb_chars=250))  # Descrição plausível ou genérica
        )
        return funcionario

    @staticmethod
    def create_batch(num, category=None):
        return [FuncionarioFactory.create(category) for _ in range(num)]
