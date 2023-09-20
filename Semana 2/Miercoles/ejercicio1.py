number1 = input("Please enter the first number\n->")
number2 = input("Please enter the second number\n->")

if number1.isnumeric():
    number1 = int(number1) 
    if number2.isnumeric():
        number2 = int(number2)
        if number2 == 0:
            print("The second number can not be 0")
        else:
            print(f"The result is {number1/number2}")
    else:
        print("The second number is not numeric")
else: 
    print("The first number is not numeric")