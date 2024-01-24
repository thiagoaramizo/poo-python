# Pilares do POO

# Herança

class Animal:
    def __init__(self, nome) -> None:
        self.nome = nome
    
    def andar(self):
        print(f"O animal {self.nome} andou!")
        return
    
    def emitir_som(self):
        pass
    
class Cachorro(Animal):
    def emitir_som(self):
        print("Au au!")
        return 

class Gato(Animal):
    def emitir_som(self):
        print("Miau!")
        return 

class Peixe(Animal):
    def andar(self):
        print(f"O animal {self.nome} não sabe andar, apenas nadar! Então nadou!")
        return
    
    def emitir_som(self):
        print("Spash Splash!")
        return 

dog = Cachorro(nome="Rex")
cat = Gato(nome="Fifi")
fish = Peixe(nome="Nemo")

dog.andar()
dog.emitir_som()
cat.andar()
cat.emitir_som()
fish.andar()
fish.emitir_som()

# Encapsulamento

class ContaBancaria:
    def __init__(self, saldo) -> None:
        self.__saldo = saldo #atributo privado

    def depositar(self, valor: int):
        if valor > 0:
            self.__saldo += valor
        return
    
    def sacar(self, valor):
        if valor > 0 and valor <= self.__saldo:
            self.__saldo -= valor
        return
    
    def consultar_saldo(self):
        return self.__saldo
    
conta1 = ContaBancaria(100)
conta1.depositar(100)
conta1.sacar(180)
print( f"O saldo da conta é {conta1.consultar_saldo()}")


# Classe Abstrata

from abc import ABC, abstractmethod

class Veiculo(ABC): #utilizando a classe ABC de lib do Python
    
    # Metodo abstrato de implementação obrigatória
    @abstractmethod
    def ligar(self):
        pass

class Carro(Veiculo):
    def __init__(self, motor) -> None:
        self.__motor = motor
    
    def ligar(self):
        print("Carro ligado!")
        return

carro_popular = Carro(motor=2.0)
carro_popular.ligar()
