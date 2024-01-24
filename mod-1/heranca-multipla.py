class Animal:
  def __init__(self, nome) -> None:
    self.nome = nome

  def emitir_som(self):
    pass

class Mamifero(Animal):
  def amamentar(self):
    print(f"{self.nome} está amamentando.")
    return

class Ave(Animal):
  def voar(self):
    print(f"{self.nome} está voando.")
    return

class Morcego(Mamifero, Ave):
  def emitir_som(self):
    print(".... (som ultrasônico)")
    return

morceguinho = Morcego(nome="Drácula")
morceguinho.emitir_som()
morceguinho.voar()
morceguinho.amamentar()