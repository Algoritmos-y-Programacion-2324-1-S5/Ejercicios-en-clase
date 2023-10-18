class Vehicle:
    def __init__(self,id, brand, model,color):
        self.id = id
        self.brand = brand
        self.model = model
        self.color = color
    
    def mostrar(self):
        return f"{self.id} - {self.brand} - {self.model} - {self.color}"