from library import Library,Book

def create_books():
    return [
        Book(1, "Harry Potter", 10),
        Book(2, "Atomic Habits", 20),
        Book(3, "The hunger games", 15),
        Book(4, "50 shades of Gray", 14),
        Book(5, "The 4 agreements", 16),
        Book(6, "The principito", 22),
        Book(7, "Lord of the rings", 45),
        Book(8, "La metamorfosis", 64),
        Book(9, "The time machine", 3),
        Book(10, "100 años de soledad", 5),
    ]

def create_library():
    return Library(1,"Pedro Grases", create_books())

def main():
    print("**** WELCOME TO SAMAN  LIBRARY ****")
    library = create_library()
    while True:
        option = input("Que accion deseas realizar: \n1-Vender\n2-Ver Inventario\n3-Añadir Libro\n4-Quitar libro\n5-Prestamo\n6- Salir\n->")
        if option == "1":
            library.show_books()
            id = int(input("Please enter the book id you want:\n"))
            library.sell_books(id)
        elif option == "2":
            library.show_books()
        elif option == "3":
            pass
        elif option == "4":
            pass
        elif option == "5":
            pass
        elif option == "6":
            print("Thank you for your visit")
            break
        else:
            print("Invalid option, please try again")


main()