# -*- coding: utf-8 -*-

from random import randint, choice, random

class Character:

    def __init__(self):
        self.name = ""
        self.health = 1
        self.health_max = 1
    
    def do_damage(self, enemy):

        damage = min(
            max(randint(0, self.health) - randint(0, enemy.health), 0),
            enemy.health
        )

        enemy.health -= damage

        if damage == 0:
            print("{} <desvia> do ataque de {}!".format(enemy.name, self.name))
        else:
            print("{} <fere> {}!".format(self.name, enemy.name))
        
        return enemy.health <= 0

class Enemy(Character):
    
    enemy_types = [
        "Caçador de Bruxas", "Vagabundo", "Gatuno",
        "Leleco", "Ximira", "Zarolho", "MORTE", "Escorropião",
        "Gato-a-Jato", "Zeca Urubú", "Brutus", "Caolho",
        "Alma Negra", "Seu Barriga", "Girafales"
    ]

    def __init__(self, player):
        Character.__init__(self)
        self.name = choice(self.enemy_types)
        self.health = randint(1, player.health)
        self.health_max = player.health_max

class Player(Character):

    def __init__(self):
        Character.__init__(self)
        self.state = "normal"
        self.health = 10
        self.health_max = 10

    def quit(self):
        self.decora()
        print("{} não consegue encontrar o caminho de volta para casa e <morre de fome>."\
        "\nR.I.P. NOOB!".format(self.name))
        self.health = 0
        self.decora()

    def decora(self):
        print("{:-^80}".format(""))
    
    def help(self):
        print(Commands.keys())

    def status(self):
        self.decora()
        if self.state != "normal":
            print("<{}>: HP({}/{})\n<{}>: HP({}/{})".format(
            self.name, self.health, self.health_max,
            self.enemy.name, self.enemy.health, self.enemy.health_max))

        else:
            print("<{}>. vitalidade: {}/{}. estado: {}".format(
            self.name, self.health,self.health_max, self.state))
        self.decora()
    
    def tired(self):
        self.decora()
        print("{} sente-se <cançado>.".format(self.name))
        self.health -= 1
        self.decora()
 
    def azar(self):
        self.decora()
        self.enemy = Enemy(self)
        print("{} teve <azar> ao encontrar-se com {}!!!".format(self.name, self.enemy.name))
        self.health = 1
        self.decora()
   
    def rest(self):
        self.decora()
        if self.state != "normal":
            print("{} não pode descansar agora!".format(self.name))
        else:
            print("{} <descansa>.".format(self.name))
  
            if randint(0, 1):
                self.enemy = Enemy(self)
                print("{} é rudemente despertado por {}!".format(
                    self.name, self.enemy.name))
                self.state = "fight"
                if self.enemy.name == "MORTE":
                    self.health = 0
                    print("{} <faleceu> ao encontrar-se com a {}!".format(
                    self.name, self.enemy.name))
                    self.enemy_attacks()
                    pass
                self.enemy_attacks()
            else:
                if self.health < self.health_max:
                    self.health += 1
                else:
                    print("{} dormiu demais!".format(self.name))
                    self.health -= 1
        self.decora()
    
    def explore(self):
        self.decora()
        if self.state != "normal":
            print("{} está muito cupado agora!".format(self.name))
            self.enemy_attacks()
        else:
            print("{} explora uma passagem sinuosa!".format(self.name))
            if randint(0, 1):
                self.enemy = Enemy(self)
                print("{} encontra {}!!!".format(self.name, self.enemy.name))
                self.state = "fight"
            else:
                if randint(0, 1):
                    self.tired()
        self.decora()
    
    def flee(self):
        self.decora()
        if self.state != "fight":
            print("{} corre em círculos por um tempo.".format(self.name))
        else:
            if randint(1, self.health+5) > randint(1, self.enemy.health):
                print("{} <foge> de {}".format(self.name, self.enemy.name))
                self.enemy = None
                self.state = "normal"
            else:
                print("{} não pode escapar de {}!".format(self.name, self.enemy.name))
                self.enemy_attacks()
        self.decora()
    
    def attack(self):
        self.decora()
        if self.state != "fight":
            print("{} golpeia o ar, sem resultados notáveis!".format(self.name))
            self.tired()
        else:
            if self.do_damage(self.enemy):
                print("{} <executa> {}!".format(self.name, self.enemy.name))
                self.enemy = None
                self.state = "normal"
                if randint(0, self.health) < 10:
                    self.health += 1
                    self.health_max += 1
                    print("{} sente-se MAIS FORTE!".format(self.name))
            else:
                self.enemy_attacks()
        self.decora()
    
    def enemy_attacks(self):
        if self.enemy.do_damage(self):
            print("{} foi <abatido> por {}!!!\nR.I.P".format(self.name, self.enemy.name))

Commands = {
    "quit": Player.quit,
    "help": Player.help,
    "status": Player.status,
    "rest": Player.rest,
    "explore": Player.explore,
    "flee": Player.flee,
    "attack": Player.attack,
}

p = Player()
p.name = input("Qual o nome do seu personagem? ")
print("(digite 'help' para uma lista de ações)\n")
print("{} entra em uma caverva escura, em busca de aventuras...".format(p.name))
p.status()

while p.health > 0:
    line = input("> ")
    args = line.split()
    if len(args) > 0:
        command_found = False
        for c in Commands.keys():
            if args[0] == c[:len(args[0])]:
                Commands[c](p)
                command_found = True
                break
        if not  command_found:
            print("{} não entendeu o comando!".format(p.name))