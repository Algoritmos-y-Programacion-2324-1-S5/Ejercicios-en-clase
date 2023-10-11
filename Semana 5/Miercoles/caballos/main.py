from horse import Horse
from race import Race
from valid import Valid

def create_horses(horses):
    horses.append(Horse("Canuto",1))
    horses.append(Horse("Vainilla",2))
    horses.append(Horse("Pastelito",3))
    horses.append(Horse("Empanada",4))
    horses.append(Horse("Bravo",5))
    horses.append(Horse("Ganador",6))

def create_race(horses, races, quantity):
    for i in range(1,quantity+1):
        races.append(Race(i,horses))

def create_valid(races,valids):
    valids.append(Valid(5,races))
    valids.append(Valid(6,races))

def main():
    """ *** INFORMACION ***
    horse = Horse("Pepito", 1)
    print(horse.show_horse())
    horse.__name = "Pepa"
    horse.set_name("pepa")
    horse.id = 2
    print(horse.show_horse())
    """
    horse_list = []
    race_list = []
    valid_list = []
    race_quantity = int(input("Cuantas carrearas deseas por valida: "))
    create_horses(horse_list)
    create_race(horse_list,race_list,race_quantity)
    create_valid(race_list,valid_list)

    for valid in valid_list:
        valid.start_valid()


    
main()