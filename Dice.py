import random


class Dice:

    @classmethod
    def lancer(cls):
        reponse = input("Lancer le dé?     o/n ---> ")
        if reponse == "o":
            var = random.randint(1, 6)
            print(f"Vous avez fait un {var}\n")
            return var
