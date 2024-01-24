from os import system
import random

class Personagem:
    """ Classe geral dos personagens """

    def __init__(self, nome, vida, nivel) -> None:
        self.__nome = nome
        self.__vida = vida
        self.__nivel = nivel

    def get_nome(self):
        return self.__nome
    
    def get_vida(self):
        return self.__vida
    
    def get_nivel(self):
        return self.__nivel
    
    def exibir_detalhes(self):
        return f"\nNome: {self.get_nome()}\nVida: {self.get_vida()}\nNível: {self.get_nivel()}"
    
    def receber_dano(self, dano):
        self.__vida -= dano
        if self.__vida < 0:
            self.__vida = 0
    
    def atacar(self, alvo):
        dano = self.__nivel * random.randint(1,3)
        alvo.receber_dano(dano)
        return f"\n{self.get_nome()} atacou {alvo.get_nome()} causando {dano} de dano!"
    
class Heroi(Personagem):
    """ Classe do herói """
    def __init__(self, nome, vida, nivel, habilidade) -> None:
        super().__init__(nome, vida, nivel)
        self.__habilidade = habilidade

    def get_habilidade(self):
        return self.__habilidade
    
    def exibir_detalhes(self):
        return f"\n{super().exibir_detalhes()}\nHabilidade: {self.get_habilidade()}"
    
    def atacar_especial(self, alvo):
        dano = self.get_nivel() * random.randint(2,5)
        alvo.receber_dano(dano)
        return f"\n{self.get_nome()} atacou {alvo.get_nome()} com a habilidade {self.get_habilidade()} causando {dano} de dano!"

class Inimigo(Personagem):
    """ Classe dos inimigos """
    def __init__(self, nome, vida, nivel, tipo) -> None:
        super().__init__(nome, vida, nivel)
        self.__tipo = tipo

    def get_tipo(self):
        return self.__tipo
    
    def exibir_detalhes(self):
        return f"{super().exibir_detalhes()}\nTipo: {self.get_tipo()}"

class Jogo:
    """ Classe orquestradora do jogo """
    def __init__(self) -> None:
        self.heroi = Heroi(nome="Herói", vida=100, nivel=5, habilidade="Super Força")
        self.inimigo = Inimigo(nome="Morcegão", vida=80, nivel=5, tipo="Voador")
        self.mensagem = ""

    def imprimir_status(self):
        system('clear')
        print( self.heroi.exibir_detalhes() )
        print( self.inimigo.exibir_detalhes() )
        return
    
    def imprimir_mensagem(self):
        print(self.mensagem)
        self.mensagem = ""

    def iniciar_batalha(self):
        """ Gerenciando a batalha em turnos """
        while self.heroi.get_vida() > 0 and self.inimigo.get_vida() > 0:
            self.imprimir_status()
            self.imprimir_mensagem()
            input( "\nPressione Enter para atacar...")
            escolha = input("\n(1) Ataque normal | (2) Ataque especial: ")

            if escolha == "1":
                self.imprimir_status()
                self.mensagem += self.heroi.atacar(self.inimigo)
                self.mensagem += self.inimigo.atacar(self.heroi)

            elif escolha == "2":
                self.imprimir_status()
                self.mensagem += self.heroi.atacar_especial(self.inimigo)
                self.mensagem += self.inimigo.atacar(self.heroi)
            else:
                print(f"\nOpção {escolha} é inválida.")

        if self.heroi.get_vida() > 0:
            self.imprimir_status()
            print("\nParabéns, você matou o inimigo!\n")
        else:
            self.imprimir_status()
            print("\nVocê morreu!\n")

# Criando instancia do jogo
jogo = Jogo()
jogo.iniciar_batalha()

