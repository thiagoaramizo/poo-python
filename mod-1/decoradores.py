def meu_decorador(func):
    def wrapper():
        print("Antes da função ser executada")
        func()
        print("Depois da função der executada")
    
    return wrapper


@meu_decorador
def minha_funcao():
    print("Função sendo executada")
    return


minha_funcao()

# Os decoradores podem ser feitos com classes
class MeuDecoradorDeClasse:
    def __init__(self, func) -> None:
        self.func = func
    
    def __call__(self) -> None:
        print("Antes da função ser executada (decorador de classe)")
        self.func()
        print("Depois da função der executada (decorador de classe)")

@MeuDecoradorDeClasse
def segunda_funcao():
    print("Executando segunda função")

segunda_funcao()