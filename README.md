# 🧮 Projeto Calculadora

## Sobre o projeto

Este projeto foi desenvolvido como atividade prática do curso de Analista de Dados da EBAC.

A aplicação consiste em uma calculadora criada em Python, capaz de realizar operações matemáticas básicas através da interação com o usuário pelo terminal.

Além do desenvolvimento em Python, o projeto utiliza um script Shell (Bash) para facilitar a execução da aplicação em ambientes Linux.

## Tecnologias utilizadas

* Python 3
* Shell Script (Bash)
* Linux (Ubuntu)
* Git
* GitHub

## Funcionalidades

A calculadora permite realizar as seguintes operações:

* Soma
* Subtração
* Multiplicação
* Divisão

Também possui tratamento para divisão por zero e um menu interativo que permanece em execução até que o usuário escolha encerrar o programa.

## Como executar

1. Abra o terminal.
2. Navegue até a pasta do projeto.
3. Conceda permissão de execução ao arquivo:

```bash
chmod 744 calculadora.sh
```

4. Execute o programa:

```bash
./calculadora.sh
```

## Estrutura do projeto

```text
projetocalculadora/
├── calculadora.py
├── calculadora.sh
├── comandos.txt
└── README.md
```

## Explicação do código

O programa solicita dois números ao usuário e apresenta um menu com as operações disponíveis.

Cada operação matemática foi implementada em uma função específica, tornando o código mais organizado, legível e fácil de manter.

Após a execução do cálculo, o programa pergunta ao usuário se deseja realizar uma nova operação. Caso a resposta seja positiva, a calculadora continua em execução utilizando um laço de repetição (`while`). Caso contrário, o programa é encerrado.

Durante o desenvolvimento foram aplicados conceitos fundamentais de programação, como:

* Variáveis
* Funções
* Estruturas condicionais (`if`, `elif` e `else`)
* Laços de repetição (`while`)
* Entrada e saída de dados
* Operações matemáticas
* Tratamento de erros

## Exemplo de utilização

```text
=== CALCULADORA ===

Digite o primeiro número: 10
Digite o segundo número: 5

Escolha uma operação:
1 - Soma
2 - Subtração
3 - Multiplicação
4 - Divisão

Opção: 3

Resultado: 50

Deseja realizar outro cálculo? (s/n): n

Programa encerrado.
```

## Objetivo

O objetivo deste projeto é praticar conceitos de programação em Python, utilização de scripts no Linux, versionamento de código com Git e publicação de projetos no GitHub.

## Autor

Eduardo Otávio

Projeto desenvolvido durante o curso de Analista de Dados da EBAC.
