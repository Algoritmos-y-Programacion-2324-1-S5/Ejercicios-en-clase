class Room:
    def __init__(self,beds, baths,price,name):
        self.name = name
        self.beds = beds
        self.baths = baths
        self.price = price
    
    def show(self):
        print(f"{self.name}\n{self.beds}\n{self.price}")

class SuiteRoom(Room):
    def __init__(self, baths, has_jacuzzi):
        super().__init__(3, baths, 100,"Suite")
        self.has_jacuzzi = has_jacuzzi

class DoubleRoom(Room):
    def __init__(self, baths, is_for_married):
        if is_for_married:
            super().__init__(1, baths, 60,"Double")
        else:
            super().__init__(2, baths, 60,"Double")
        self.is_for_married = is_for_married

class SingleRoom(Room):
    def __init__(self, baths,has_tv):
        super().__init__(1, baths, 40, "Simple")
        self.has_tv = has_tv
        

        