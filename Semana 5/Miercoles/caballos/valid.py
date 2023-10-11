class Valid:
    def __init__(self, id, races):
        self.id = id
        self.races = races

    def start_valid(self):
        print("La valida {} esta iniciando, todos preparados...!")
        for race in self.races:
            race.start_race()
            race.choose_winner()