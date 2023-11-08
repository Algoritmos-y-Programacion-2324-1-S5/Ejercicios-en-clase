from room import SingleRoom, SuiteRoom,DoubleRoom
from order import Order
from customer import Customer

def print_stats():
    pass

def register():
    name = input("Please enter the customer name: ")
    age = input("Please enter the customer age: ")
    id = input("Please enter the customer id: ")
    phone = input("Please enter the customer phone: ")
    quantity = input("Please enter the customer quantity people: ")
    order_list = []
    customer = Customer(name,age,id,phone,quantity)
    while True:
        room_option = input("Please enter the room you want \n1-Suite\n2-Double\n3-Simple\n")
        nights = int(input("Please select how many nights the customer wants: "))
        if room_option == "1":
            room = SuiteRoom(3,True)
        elif room_option == "2":
            room = DoubleRoom(2, True)
        else: 
            room = SingleRoom(1, True)
        order_list.append(Order(room,nights))
        exit_option = input("Do you want to make another book: 1-Yes / 2-No:")
        if exit_option == "2":
            break
    print("***** RECEIPT *****")
    customer.show_customer()
    total = 0
    for order in order_list:
        order.room.show()
        total += (order.room.price*order.nigths)


def main():
    print("*** WELCOME TO SAMAN HOTELS ***")
    while True:
        option = input("Please enter a valid option \n1-Register a customer\n2-Exit\n->")
        if option == "2":
            print("Thank you for your visit!")
            print_stats()
            break
        else:
            register()

main()