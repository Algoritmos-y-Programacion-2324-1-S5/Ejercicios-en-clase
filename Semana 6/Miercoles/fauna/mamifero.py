from animals import Animal

class Mamifero(Animal):

    def __init__(self, color, name, id, havePaws, habitat):
        super().__init__(color, "Mamifero", name, id)
        self.havePaws = havePaws
        self.habitat = habitat

class MamiferoAcuatico(Mamifero):

    def __init__(self, color, kind, name, id, havePaws):
        super().__init__(color, kind, name, id, havePaws, "Acuatico")

class MamiferoTerrestre(Mamifero):

    def __init__(self, color, name, id, havePaws):
        super().__init__(color, name, id, havePaws, "Tierra")

