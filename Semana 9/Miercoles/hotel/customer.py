class Customer:
    def __init__(self,name,age,id,phone,people_quantity):
        self.name = name
        self.age = age
        self.id = id
        self.phone = phone
        self.people_quantity = people_quantity
    
    def show_customer(self):
        print(f"{self.name}\n{self.age}\n{self.id}\n{self.phone}\n{self.people_quantity}")