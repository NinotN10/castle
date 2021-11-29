from Items import Sword, Potion
from Monster import KingSkull, Spider, Zombie, Bat


class Castle:
    @classmethod
    def board(cls):
        case = dict.fromkeys([*range(18)])
        sword = Sword()
        potion = Potion()
        skullking = KingSkull()
        bat = Bat()
        zombie = Zombie()
        spider = Spider()
        case[2] = bat
        case[5] = zombie
        case[10] = potion
        case[12] = potion
        case[15] = spider
        case[16] = skullking
        case[17] = sword
        return case
