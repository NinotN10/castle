from Castle import Castle
from Dice import Dice
from Items import Sword, Potion
from Monster import Monster


class Hero:
    max_life = 5
    max_position = len(Castle.board()) - 1

    def __init__(self):
        self.position = 0
        self.life = 3
        self.sword = False
        self.death = False

    def move(self):
        if self.position < len(Castle.board()):
            self.position += Dice.lancer()
            self.position = min(self.position, Hero.max_position)
            print(f"Vous êtes à la case {self.position}")
            self.fight(self.position, Castle.board())
            self.take_potion(self.position, Castle.board())
            self.take_sword(self.position, Castle.board())
        return self.position

    def take_sword(self, position, case):
        if isinstance(case[position], Sword):
            print(f"Vous avez trouvé l'épée à la case {position}, félicitation vous avez fini le jeu\n")
            self.sword = True
            return self.sword

    def take_potion(self, position, case):
        if isinstance(case[position], Potion):
            self.life += 1
            self.life = min(self.life, Hero.max_life)
            print(f"Vous avez trouvé une potion de soin, vont points de vie sont à {self.life}\n")

    def fight(self, position, case):
        if not isinstance(case[position], Monster):
            return
        print(f"Vous venez de tomber sur le monstre {case[position].name}, de niveau {case[position].level}\n")
        monster = case[position]
        while self.life > 0 or monster is not None:
            if monster.level == 1:
                print('Vous devez lancer le dé\n'
                      'si si le résultat est 1 ou 2 : le héros perd 1 point de vie\n'
                      'si le résultat est 3, 4, 5, 6 : le héros ne perd pas de point de vie.\n')

                dice = Dice.lancer()
                if dice in [1, 2]:
                    self.less_life(1)
                else:
                    return Hero.kill_monster(monster)

            if monster.level == 2:
                print('Vous devez lancer le dé\n'
                      'si si le résultat est 1, 2 ou 3 : le héros perd 1 point de vie\n'
                      'si le résultat est 4, 5, 6 : le héros ne perd pas de point de vie.\n')

                dice = Dice.lancer()
                if dice in [1, 2, 3]:
                    self.less_life(1)
                else:
                    return Hero.kill_monster(monster)

            if monster.level == 3:
                print('Vous devez lancer le dé\n'
                      'si si le résultat est 1, 2 ou 3 : le héros perd 2 point de vie\n'
                      'si le résultat est 4, 5, 6 : le héros ne perd pas de point de vie.\n')

                dice = Dice.lancer()
                if dice in [1, 2, 3]:
                    self.less_life(2)
                else:
                    return Hero.kill_monster(monster)

        if self.life <= 0:
            self.death = True
            print("\nVous êtes mort, GAME OVER!! :( \n")

    def less_life(self, degat):
        self.life -= degat
        print(f"\nVous avez perdu {degat} point de vie!!!!!! Il vous reste {self.life}\n")

    @staticmethod
    def kill_monster(monster):
        print(f"Vous avez vaincu le {monster.name}!!!!\n")
        monster = None
        return monster
