import random

class Race:
    def __init__(self, id, horses):
        self.id = id
        self.horses = horses

    def start_race(self):
        print("Partidaaaaaaaaaaaaaaaaaaaaaa saliron los competidores")
        print(f"En la carrera {self.id} se encuentran corriendo:")
        for horse in self.horses:
            print(f"{horse.show_horse()}")

    def choose_winner(self):
        winner = random.choice(self.horses)
        print(f"***************** The winner is {winner.show_horse()} *****************")