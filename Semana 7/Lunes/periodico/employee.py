class Employee:
    def __init__(self, id, name, dni, role):
        self.id = id
        self.name = name
        self.dni = dni
        self.role = role
    
    def show_employee(self):
        return f"id: {self.id} - Name: {self.name} - Role: {self.role}"

class Writer(Employee):

    def __init__(self, id, name, dni):
        super().__init__(id, name, dni, "Writer")

    def write_article(self):
        print("Writing article...")

class Boss(Employee):
    def __init__(self, id, name, dni):
        super().__init__(id, name, dni, "Boss")
    
    def validate_writers(self):
        print("Everything is ok")

    def validate_article(self, article):
        print("El articulo fue aprobado")