### Início Rápido

Este comando é usado para executar as etapas rápidas e iniciar o ambiente virtual com as dependências e, em seguida, iniciar o servidor.

~~~
    bash test.sh
~~~

#### Requisitos do Sistema

Para criar aplicativos web com DRF, você precisará incluir os seguintes requisitos em seu sistema:

- Python 3.10 ou uma versão mais recente;
- Pip 22.0 ou uma versão mais recente;
- Virtualenv 20.19 ou uma versão mais recente;

#### Instalação Manual

Este guia tem como objetivo dar um salto inicial nas configurações do projeto e trazer um projeto DRF prático e rápido. No entanto, para habilitar e executar o projeto, alguns comandos ainda são necessários.

- **Passo 1** - Crie um ambiente virtual python para instalar todas as dependências necessárias:
~~~
    python3 -m venv venv
~~~

- **Passo 2** - Ative o ambiente virtual python:
 
_Linux_
~~~
    . venv/bin/activate
~~~
_Windows_
~~~
    .\venv\Scripts\activate
~~~

- **Passo 3** - Instale todas as dependências:
~~~
    pip install -r requirements.txt
~~~

- **Passo 4** - Execute um servidor interno e divirta-se! ;)
~~~
    python manage.py runserver
~~~

Pare o servidor digitando Ctrl+C no terminal.

#### Comandos Adicionais

- **Migrações de Banco de Dados**
~~~
    python manage.py makemigrations
    python manage.py migrate
~~~

- **Popular Banco de Dados com Dados de Factory**
~~~
    python manage.py populate_db
~~~

Este projeto é baseado no [LISA DRF Quick Project!](<https://github.com/lisa-ufersa/django-quickproject>)

### Projeto constantemente testado pelo SonarQube Cloud

[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=DanielLinsAndrade_Gerenciamento-de-inventario&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=DanielLinsAndrade_Gerenciamento-de-inventario)

## Sobre o Projeto

O sistema permite que usuários gerenciem itens e categorias no inventário, garantindo uma visão clara sobre o estoque e suas quantidades. Ele pode ser utilizado por dois tipos de usuários, cada um com permissões específicas.

Os caminhos: /inventory e /usuario

Principais Funcionalidades
Categorias, Itens e Usuários:

- Inventory: Possui grupos que organizam os itens de maneira lógica (ex.: Eletrônicos, Móveis, Roupas). Também possui Itens, que são produtos específicos que pertencem a uma categoria e possuem atributos como nome, quantidade, preço, e descrição.
- Usuario: Campo destinado para cadastrar dois tipos de usuários como gerente e funcionario.
