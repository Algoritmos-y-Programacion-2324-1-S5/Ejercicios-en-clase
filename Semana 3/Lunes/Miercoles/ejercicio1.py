heigth = int(input("Please enter the heigth: "))
for number in range(1,heigth*2,2): 
    for index in range(number,0,-2):
        print(index,end = " ")
    print()