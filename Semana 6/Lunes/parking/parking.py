class ParkingLot:
    def __init__(self, id, cars):
        self.id = id
        self.cars = cars
        self.spaces = 50

    def get_in(self, car):
        self.cars.append(car)
        self.spaces = self.spaces - 1

    def get_out(self): 
        pass
















    