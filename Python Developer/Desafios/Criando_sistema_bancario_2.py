import textwrap
from abc import ABC, abstractclassmethod, abstractproperty
from datetime import datetime


class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)

class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf

class Conta:
    def def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)

    @property
    def saldo(self):
        return self._saldo

    @property
    def numero(self):
        return self._numero
   
   @property
    def agencia(self):
        return self._agencia
   
   @property
    def cliente(self):
        return self._cliente
   
   @property
    def historico(self):
        return self._historico

def sacar(self, valor):
    saldo = self.saldo
    excedeu_saldo = valor > saldo

    if excedeu_saldo:
        print("\n@@@ Saldo insuficiente!")
    
    elif valor > 0:
        self._saldo -= valor
        print("\n=== Saque realizado com sucesso! ===")
        return True

    else:
        print("\n@@@ Operação falhou! Valor informado invalido.")
        return False

def depoistar(self, valor):
    if valor > 0:
        self._saldo += valor
        print("===\n O dinheiro foi depositado com sucesso!===")
    else:
        print("\n@@@ Operação falhou! Valor informado é invalido!")

    return True

class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self._limite = limite
        self._limite_saques = _limite_saques
    
    def sacar(self, valor):
        numero_saques = len(
            [transicap for transicao in self.historico.transicoes if transicao["tipo"] == Saque.__name__]
        )

        excedeu_limite = valor > self.limite
        excedeu_saques = numero_saques >= self._limite_saques

        if excedeu_limite:
            print("\n@@@ O valor do saque excede o seu limite atual. @@@")
        
        elif excedeu_saques:
            print ("\n@@@ Você excedeu seus saques diarios, por favor aguarte até amanhã ou cantate o banco.")
        
        else:
            return super().sacar(valor)
        
        return False

