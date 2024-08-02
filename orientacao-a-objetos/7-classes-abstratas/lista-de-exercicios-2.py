# O banco Banco Delas é um banco moderno e eficiente, com vantagens exclusivas para clientes mulheres.
# Modele um sistema orientado a objetos para representar contas correntes do Banco Delas seguindo os requisitos abaixo.

# 1. Cada conta corrente pode ter um ou mais clientes como titular.
# 2. O banco controla apenas o nome, o telefone e a renda mensal de cada cliente.
# 3. A conta corrente apresenta um saldo e uma lista de operações de saques e depósitos.
#    Quando a cliente fizer um saque, diminuiremos o saldo da conta corrente. Quando ela 
#    fizer um depósito, aumentaremos o saldo.
# 4. Clientes mulheres possuem em suas contas um cheque especial de valor igual à sua renda
#    mensal, ou seja, elas podem sacar valores que deixam a sua conta com valor negativo até
#    -renda_mensal.
# 5. Clientes homens por enquanto não têm direito a cheque especial.

# Para modelar seu sistema, utilize obrigatoriamente os conceitos "classe", "herança", "propriedades", 
# "encapsulamento" e "classe abstrata".

from abc import ABC, abstractmethod

class Cliente(ABC):
    def __init__ (self, nome, telefone, renda_mensal):
        self._nome = nome
        self._telefone = telefone
        self._renda_mensal = renda_mensal

    @property
    def nome(self):
        return self._nome

    @property
    def telefone(self):
        return self._telefone

    @property
    def renda_mensal(self):
        return self._renda_mensal

    @abstractmethod
    def possui_cheque_especial(self):
        pass

class ClienteMulher(Cliente):
    def possui_cheque_especial(self):
        return self._renda_mensal

class ClienteHomem(Cliente):
    def possui_cheque_especial(self):
        return 0
    
class ContaCorrente:
    def __init__(self):
        self._saldo = 0
        self._operacoes = []
        self._titulares = []

    @property
    def saldo(self):
        return self._saldo

    @property
    def operacoes(self):
        return self._operacoes

    def adicionar_titular(self, cliente):
        if isinstance(cliente, Cliente):
            self._titulares.append(cliente)
        else:
            raise ValueError("Titular deve ser uma instância de Cliente")

    def depositar(self, valor):
        if valor <= 0:
            raise ValueError("O valor do depósito deve ser positivo")
        self._saldo += valor
        self._operacoes.append(f"Depósito de R$ {valor:.2f}")

    def sacar(self, valor):
        if valor <= 0:
            raise ValueError("O valor do saque deve ser positivo")

        cheque_especial_disponivel = max([titular.possui_cheque_especial() for titular in self._titulares])
        if self._saldo - valor < -cheque_especial_disponivel:
            raise ValueError("Saldo insuficiente, considerando cheque especial")
        
        self._saldo -= valor
        self._operacoes.append(f"Saque de R$ {valor:.2f}")

cliente1 = ClienteMulher(nome="Ana", telefone="123456789", renda_mensal=3000)
cliente2 = ClienteHomem(nome="Carlos", telefone="987654321", renda_mensal=5000)

conta = ContaCorrente()
conta.adicionar_titular(cliente1)
conta.adicionar_titular(cliente2)

conta.depositar(10000)
print(conta.saldo)  

conta.sacar(2000)
print(conta.saldo)  

print(conta.operacoes)
