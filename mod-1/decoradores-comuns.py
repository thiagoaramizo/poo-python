# São os decoradores mais comumente utilizados
# @classmethod e @staticmethod

class MinhaClasse:
    
    valor = 10 #atributo da classe

    def __init__(self, nome) -> None:
        self.nome = nome  #atributo da instancia

    def metodo_da_instancia(self): #metodo da instância, só pode ser chamada por uma instância
        print(f"método da instância! O nome da instancia é {self.nome}")
        return
    
    @classmethod
    def metodo_da_classe(cls):
        print(f"Método da classe. O valor da classe é {cls.valor}")
        return
    
    @staticmethod
    def metodo_estatico(): #metodo estático, não tem acesso a atributos
        print(f"Método estatico da classe;")
        return

objeto = MinhaClasse(nome="meu objeto")    
print( MinhaClasse.valor )
print( objeto.valor )