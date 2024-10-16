# Modelando o Sistema Bancário em POO com Python

## Introdução

Este repositório contém a solução para o desafio "Modelando o Sistema Bancário em POO com Python", parte do bootcamp "NTT DATA - Engenharia de Dados com Python". O objetivo deste projeto foi refatorar o sistema bancário otimizado pelo uso de funções para o paradigma POO, adotando boas práticas de programação.

## Desafio

### Objetivo do Desafio

O desafio consiste em refatorar o código de um sistema bancário, aplicando boas práticas de programação OO. O sistema tem fins didáticos e inclui operações básicas de um banco, como saques, depósitos, extrato bancário e controle de limites.

### Funcionalidades Implementadas

- Depósitos: Permite ao usuário depositar valores em sua conta.
- Saques: Controle de limite e número de saques permitidos por dia.
- Extrato: Mostra todas as movimentações da conta e o saldo atual.
- Validações de Transações: Garantia de que as transações ocorram dentro dos limites estabelecidos.
- Menu Interativo: Apresentação das opções disponíveis de forma clara e organizada.

# Solução Proposta

A solução foi implementada em Python (versão 3.12.6), sem a utilização de frameworks ou bibliotecas externas. Todo o sistema foi construído com base em POO.

### Estrutura do Projeto

- main.py: Arquivo principal responsável por executar o sistema.
- service_account.py: Gerencia as operações bancárias, como saques, depósitos e extrato.
- service_validation.py: Funções de validação para garantir a integridade das operações.
- utils_print.py: Funções auxiliares para impressão e formatação de menus no console.
- type_define.py: Definições de tipos para as transações e contas.
- util_create_new_user.py: Funções para criação de novas contas de usuário.

## Executando o Projeto

Para rodar o projeto em seu ambiente, siga os passos abaixo:

Clone este repositório:

```bash
git clone https://github.com/andreluizmb82/2-otimizando-o-sistema-banc-rio-com-fun-es-python.git
```

Entre no diretório do projeto e execute o arquivo main.py:

No Windows:

```bash
python main.py
```

No Linux:

```bash
python3 main.py
```

## Considerações Finais

Este projeto didático foi uma oportunidade prática para aplicar conceitos básicos de POO em Python, mantendo o código modular e fácil de manter. Além disso, ele exemplifica como estruturar um sistema bancário básico, com fins didáticos, sem o uso de POO, focando em simplicidade e manutenibilidade.
