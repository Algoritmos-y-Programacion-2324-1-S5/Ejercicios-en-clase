def show_welcome():
    print("*********** Welcome to the UNIMET DIGITAL STORE ***********")

def show_menu():
    option = input("Please enter a valid option:\n1-Show Inventory\n2-Buy\n3-Apply Promo\n4-Exit\n->")
    return option

def show_inventory(products_to_use):
    category = input("Please enter a category\n1-Mobiles\n2-Laptops\n->")
    if category == "1":
        category = "mobiles"
    else:
        category = "laptops"

    devices = products_to_use.get(category)
    for brand, product_list in devices.items():
        print("***",brand,"***")
        for product in product_list:
            for key, value in product.items():
                print(key.title(),value,sep=" - ", end= " / " )
            print()
    

def main():
    products = {
        "mobiles": {
            "Apple": [
                {
                    "id": 1,
                    "name": "iPhone 7",
                    "price": 300
                },
                {
                    "id": 2,
                    "name": "iPhone 8",
                    "price": 350
                },
                {
                    "id": 3,
                    "name": "iPhone Xr",
                    "price": 450
                },
                {
                    "id": 4,
                    "name": "iPhone Xs",
                    "price": 460
                },
                {
                    "id": 5,
                    "name": "iPhone 11",
                    "price": 900
                },
                {
                    "id": 6,
                    "name": "iPhone 12",
                    "price": 1100
                },
                {
                    "id": 7,
                    "name": "iPhone 13",
                    "price": 1300
                },
            ],
            "Samsung": [
                {
                    "id": 8,
                    "name": "Samsung Galaxy Beam",
                    "price": 150
                },
                {
                    "id": 9,
                    "name": "Samsung Galaxy S6",
                    "price": 200
                },
                {
                    "id": 10,
                    "name": "Samsung Galaxy S7",
                    "price": 300
                },
            ],
            "Xiaomi": [
                {
                    "id": 11,
                    "name": "Xiaomi Redmi Note 8",
                    "price": 250
                },
                {
                    "id": 12,
                    "name": "Xiaomi Redmi Note 8 Pro",
                    "price": 300
                },
            ]
        },
        "laptops": {
            "DELL": [
                {
                    "id": 13,
                    "name": "Dell Inspiron 15",
                    "price": 600
                },
                {
                    "id": 14,
                    "name": "Dell Latitude 14",
                    "price": 650
                },
            ],
            "MAC": [
                {
                    "id": 15,
                    "name": "MacBook Pro 13",
                    "price": 900
                },
                {
                    "id": 16,
                    "name": "MacBook M1",
                    "price": 1500
                },
            ]
        },
    }
    show_welcome()
    while True:
        option = show_menu()
        if option == "1":
            show_inventory(products)
        elif option == "2":
            pass
        elif option == "3":
            pass
        elif option == "4":
            print("Thank you for your visit")
            break
        else:
            print("Error option, try again")

main()
