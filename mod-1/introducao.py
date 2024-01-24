
# Classe Pessoa

class Pessoa:
    def __init__(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade
    
    def se_apresentar(self):
        print("Meu nome é " + self.nome + " e minha idade é " + str(self.idade) + " anos.")


# Objetos
        
pessoa1 = Pessoa("Thiago", 34)
pessoa2 = Pessoa("Julia", 28)

pessoa1.se_apresentar()
pessoa2.se_apresentar()