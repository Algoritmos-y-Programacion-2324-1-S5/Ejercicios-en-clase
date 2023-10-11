class Horse:
    def __init__(self, nombre, identification):
        self.__name = nombre
        self.id = identification

    def set_name(self,name):
        self.__name = name

    def show_horse(self):
        return f"{self.id} - Horse: {self.__name}"