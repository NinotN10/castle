class Items:

    def __init__(self, name=None, type_objet=None):
        self.name = name
        self.type_objet = type_objet

    def __repr__(self):
        return self.__class__.__name__


class Sword(Items):
    def __init__(self, name="sword", type_object="weapon"):
        super().__init__(name, type_object)


class Potion(Items):
    def __init__(self, name="potion", type_objet="soin"):
        super().__init__(name, type_objet)
