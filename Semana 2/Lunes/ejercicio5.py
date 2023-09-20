money = input("Please enter the money amount that you will deposit:")
money = float(money)
interes_quantity = 1.04
interes = 0.04
year1 = money*interes_quantity
#year1 = money + (money * interes)
year2 = year1*interes_quantity
year3 = year2*interes_quantity
print("Your money for year 1 is: $"+str(round(year1,2)))
print("Your money for year 2 is: $"+str(round(year2,2)))
print("Your money for year 3 is: $"+str(round(year3,2)))