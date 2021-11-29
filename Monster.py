class Monster:

    def __init__(self, name, level):
        self.name = name
        self.level = level

    def __repr__(self):
        return self.__class__.__name__


class KingSkull(Monster):
    def __init__(self, name="King Skull", level=3):
        super().__init__(name, level)


class Bat(Monster):
    def __init__(self, name="Bat", level=1):
        super().__init__(name, level)


class Zombie(Monster):
    def __init__(self, name="Zombie", level=1):
        super().__init__(name, level)


class Spider(Monster):
    def __init__(self, name="Spider", level=2):
        super().__init__(name, level)
