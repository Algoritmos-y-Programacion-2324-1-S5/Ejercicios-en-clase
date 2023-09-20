pizza_type = input("Please select a pizza type:\n1- Vegetarian\n2- No Vegetarian")

if pizza_type == "1":
    print("The available ingredients are: \n1-Pimiento\n2-Tofu")
    ingredient = ""
    selected_ingredient = input("Please select one:")
    if selected_ingredient == "1":
        ingredient = "Pimiento"
    else:
        ingredient = "Tofu"
    print(f"The pizza is vegetarian and have tomato, mozzarella and {ingredient}")
elif pizza_type == "2":
    print("The available ingredients are: \n1-Peperoni\n2-Jam\n3-Salmon")
    ingredient = ""
    selected_ingredient = input("Please select one:")
    if selected_ingredient == "1":
        ingredient = "Peperoni"
    elif selected_ingredient == "2":
        ingredient = "Jam"
    else:
        ingredient = "Salmon"
    print(f"The pizza is vegetarian and have tomato, mozzarella and {ingredient}")
else:
    print("Invalid option")