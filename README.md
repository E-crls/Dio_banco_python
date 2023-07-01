# Sistema Bancário Simples em Python

Este projeto é uma implementação simples de um sistema bancário em Python. O sistema suporta operações básicas como depósito, saque e consulta de saldo.

## Implementação

A implementação consiste em duas classes principais: `Banco` e `ContaBancaria`.

`ContaBancaria` é uma classe que representa uma conta bancária individual. Ela tem métodos para depositar, sacar e ver o saldo.

`Banco` é uma classe que representa o banco em si. Ele tem um dicionário de contas que pode ser acessado por número de conta. Ele tem métodos para criar uma nova conta, depositar dinheiro em uma conta, sacar dinheiro de uma conta e ver o saldo de uma conta.

## Como usar

Primeiro, instancie a classe `Banco`:

banco = Banco()

Para criar uma nova conta, use o método criar_conta e passe o número da conta como um argumento:

banco.criar_conta('12345678')

Para depositar dinheiro em uma conta, use o método deposito e passe o número da conta e o valor do depósito como argumentos:

banco.deposito('12345678', 1000)

Para sacar dinheiro de uma conta, use o método saque e passe o número da conta e o valor do saque como argumentos:

banco.saque('12345678', 500)

Para ver o saldo de uma conta, use o método extrato e passe o número da conta como um argumento:

banco.extrato('12345678')

Notas

Este é um projeto simples e serve apenas para fins educacionais. Em um sistema bancário real, seria necessário considerar muitos outros fatores, como autenticação do usuário, armazenamento seguro dos dados da conta, histórico de transações, etc.

Além disso, este projeto não inclui a monetização de operações. Se o banco desejasse cobrar uma taxa por certas operações, seria possível adicionar uma taxa ao método saque que seria subtraída do saldo da conta juntamente com o valor do saque.
