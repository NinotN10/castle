from Hero import Hero


class Party:
    @classmethod
    def party(cls):
        hero = Hero()
        play = True
        input("Choissez votre nom:   \n")
        while hero.sword is not True and play and hero.death is not True:
            hero.move()

