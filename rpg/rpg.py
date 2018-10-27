# -*- coding: utf-8 -*-

from random import randint, choice, random
from art import tprint
import colorama
colorama.init()


COR = colorama.Fore.LIGHTRED_EX
RESET_COR = colorama.Style.RESET_ALL


class Character:

    def __init__(self):
        self.name = ""
        self.health = 10
        self.health_max = 10

    def do_damage(self, enemy):

        damage = min(
            max(randint(0, self.health) - randint(0, enemy.health), 0),
            enemy.health
        )

        enemy.health -= damage

        if damage:
            print(COR + self.name + RESET_COR + " <fere> " +
                  COR + enemy.name + RESET_COR + " com " + COR + 
                  str(damage) + " de dano!" + RESET_COR)
        else:
            print(COR + enemy.name + RESET_COR +
                  " <desvia> do ataque de " + COR + self.name + RESET_COR)

        return enemy.health <= 0


class Enemy(Character):

    enemy_types = ["Caçador de Bruxas", "Vagabundo", "Gatuno",
                   "Leleco", "Ximira", "Zarolho", "MORTE", "Escorropião",
                   "Gato-a-Jato", "Zeca Urubu", "Brutus", "Caolho",
                   "Alma Negra", "Seu Barriga", "Girafales", "Irmãos Neto",
                   "Lula Molusco", "Sirigueijo"]

    def __init__(self, player):
        Character.__init__(self)
        self.name = choice(self.enemy_types)
        self.health = 10
        self.health_max = 10


class Player(Character):

    motivos_da_morte = ["de fome", "doente", "afogado", "caindo no abismo",
                        "atacado por vadios", "escravisado", "estrangulado",
                        ]

    def __init__(self):
        Character.__init__(self)
        self.state = "normal"
        self.health = 10
        self.health_max = 10

    def quit(self):
        self.decora()
        print(COR + self.name + RESET_COR +
              " não consegue encontrar o caminho de volta para casa e morre " +
              COR + choice(self.motivos_da_morte) + "\nR.I.P. NOOB!")
        self.health = 0
        self.game_over()
        print(colorama.Style.RESET_ALL)
        self.decora()

    def decora(self):
        print(colorama.Fore.BLUE)
        print("{:-^80}".format(""))
        print(RESET_COR)

    def help(self):
        print(Commands.keys())

    def status(self):
        self.decora()
        if self.state != "normal":
            print("Player: " + COR + self.name + RESET_COR +
                  " HP: " + COR + str(self.health) + "/" + str(self.health_max) +
                  RESET_COR + " Status: " + COR + self.state + "\n" + RESET_COR +
                  "Enemy: " + COR + self.enemy.name + RESET_COR + " HP: " +
                  COR + str(self.enemy.health) + "/" + str(self.enemy.health_max) +
                  RESET_COR)
        else:
            print("Player: " + COR + self.name + RESET_COR +
                  " HP: " + COR + str(self.health) + "/" + str(self.health_max) +
                  RESET_COR + " Status: " + COR + self.state + RESET_COR)
        self.decora()

    def tired(self):
        self.decora()
        print(COR + self.name + RESET_COR + " sente-se <cançado>.")
        self.health -= 1

    def azar(self):
        self.decora()
        self.enemy = Enemy(self)
        print(f"{self.name} teve <azar> ao encontrar-se com {self.enemy.name}!!!")
        self.health = 1
        self.decora()

    def rest(self):
        self.decora()
        if self.state != "normal":
            print(COR + self.name + RESET_COR + " não pode descansar agora!")
        else:
            print(COR + self.name + RESET_COR + " <descansa>.")

            if randint(0, 1):
                self.enemy = Enemy(self)
                print(COR + self.name + RESET_COR +
                      " é rudemente despertado por " + COR +
                      self.enemy.name + RESET_COR)
                self.state = "fight"
                if self.enemy.name == "MORTE":
                    self.health = 0
                    print(COR + self.name + RESET_COR +
                          " <faleceu> ao encontrar-se com " + COR +
                          self.enemy.name + RESET_COR)
                    self.enemy_attacks()
                    pass
                self.enemy_attacks()
            else:
                if self.health < self.health_max:
                    self.health += 1
                else:
                    print(COR + self.name + RESET_COR + " dormiu demais!.")
                    self.health -= 1
        self.decora()

    def explore(self):
        self.decora()
        if self.state != "normal":
            print(COR + self.name + RESET_COR + " está muito cupado agora!")
            self.enemy_attacks()
        else:
            print(COR + self.name + RESET_COR +
                  " explora uma passagem sinuosa!")
            if randint(0, 1):
                self.enemy = Enemy(self)
                print(COR + self.name + RESET_COR + " encontra com " +
                      COR + self.enemy.name + RESET_COR)
                self.state = "fight"
                if self.enemy.name == "MORTE":
                    self.health = 0
                    print(COR + self.name + RESET_COR +
                          " <faleceu> ao encontrar-se com " + COR +
                          self.enemy.name + RESET_COR)
                    self.enemy_attacks()
            else:
                if randint(0, 1):
                    self.tired()
        self.decora()

    def flee(self):
        self.decora()
        if self.state != "fight":
            print(COR + self.name + RESET_COR +
                  " corre em círculos por um tempo.")
        else:
            if randint(1, self.health+5) > randint(1, self.enemy.health):
                print(COR + self.name + RESET_COR + " <foge> de " +
                      COR + self.enemy.name + RESET_COR)
                self.enemy = None
                self.state = "normal"
            else:
                print(COR + self.name + RESET_COR + " não pode escapar de " +
                      COR + self.enemy.name + RESET_COR)
                self.enemy_attacks()
        self.decora()

    def attack(self):
        self.decora()
        if self.state != "fight":
            print(COR + self.name + RESET_COR +
                  " golpeia o ar, sem resultados notáveis!")
            self.tired()
        else:
            if self.do_damage(self.enemy):
                print(COR + self.name + RESET_COR +
                      " <executa> " + COR + self.enemy.name + RESET_COR)
                self.enemy = None
                self.state = "normal"
                if randint(0, self.health) < 10:
                    self.health += 1
                    self.health_max += 1
                    print(COR + self.name + RESET_COR + " sente-se MAIS FORTE!")
            else:
                self.enemy_attacks()
        self.decora()

    def enemy_attacks(self):
        if self.enemy.do_damage(self):
            print(COR + self.name + RESET_COR + " foi <abatido> por " +
                  COR + self.enemy.name + "\nR.I.P" + RESET_COR)
            self.state = 'MORTO'
            
            self.status()
            self.game_over()

    def game_over(self):
        print(colorama.Fore.RED)
        tprint('You Die!', font='poison')
        print(colorama.Style.RESET_ALL)

    def show_menu(self):
        print("Ações:")
        print(COR + "1: quit" + RESET_COR)
        print("2: help")
        print("3: status")
        print("4: rest")
        print("5: explore")
        print("6: flee")
        print("7: attack")

        line = input("> ")
        args = line.split()
        return args


Commands = {
    "1": Player.quit,
    "2": Player.help,
    "3": Player.status,
    "4": Player.rest,
    "5": Player.explore,
    "6": Player.flee,
    "7": Player.attack
}

p = Player()
print(colorama.Fore.LIGHTYELLOW_EX)
tprint('RPG', font='georgia11')
print(colorama.Style.RESET_ALL)
p.name = input("Qual o nome do seu personagem? ")
print("(digite 'help' para uma lista de ações)\n")
print(f"{p.name} entra em uma caverva escura, em busca de aventuras...")
p.status()

while p.health > 0:
    action = p.show_menu()
    if len(action) > 0:
        command_found = False
        for c in Commands.keys():
            if action[0] == c[:len(action[0])]:
                Commands[c](p)
                command_found = True
                break
        if not command_found:
            print(COR + p.name + " não entendeu o comando! " + RESET_COR)
