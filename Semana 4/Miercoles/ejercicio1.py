def ejercicio1(n):
    final_list = []
    #acum_suma = 0
    for number in  range(1,n+1):
        if number % 3 == 0 or number % 5 == 0 or number % 7 == 0:
           #acum_suma += number
            final_list += [number]
    #print("Result suma", acum_suma) 
    print("Result lista", sum(final_list)) 

def ejercicio2(n):
    lista = []
    #for number in range(1,(n+1)//2):
    #    lista.append(number)
    #    lista.append(number*-1)
    for number in range(1,n):
        lista.append(number)
    lista.append(sum(lista)*-1)

    print("La lista final fue:", lista)
    print("La suma da: ",sum(lista))

def is_prime(number):
    if number < 2:
        return False
    else:
        aux = number - 1
        while aux > 1:
            if number % aux == 0:
                return False
            aux -=1
        return True

def ejercicio3():
    player_1 = [4,10,7,9]
    player_2 = [6,5,2,3]
    result_player1 = calculate_result(player_1)
    result_player2 = calculate_result(player_2)
    print("El score del player 1 es:", result_player1)
    print("El score del player 2 es:", result_player2)
    if result_player1 == result_player2:
        return 0
    elif result_player1 > result_player2:
        return 1
    else: 
        return 2
    
    
def calculate_result(lista_puntuacion):
    result = 0
    if 10 in lista_puntuacion:
        cont = 0
        for puntuacion in lista_puntuacion:
            result += puntuacion
            if cont > 0:
                result += puntuacion
                cont -= 1
            if puntuacion == 10:
                cont +=2 
    else:
        result = sum(lista_puntuacion)
    
    return result

def ejercicio4():
    nums = [[1,2,3], [5,6,7], [9,10,11]]
    primo = 0
    for i, lista in enumerate(nums):
        for j, number in enumerate(lista):
            if i == j or j == (len(nums) - i - 1):
                print("numbers", number)
                is_primo = is_prime(number)
                if is_primo:
                    if number > primo:
                        primo = number
    print("El primo mayor es", primo)

def main():
    option = input("Please enter a option:\n1-Ejercicio1\n2-Ejercicio2\n3-Ejercicio3\n4-Ejercicio4\n->")
    if option == "1":
        print("***** Ejercicio 1 *****")
        ejercicio1(int(input("Please enter a number to evaluate:")))
    elif option == "2":
        print("***** Ejercicio 2 *****")
        ejercicio2(int(input("Please enter a number to evaluate:")))
    elif option == "3":
        print("***** Ejercicio 3 *****")
        print("El ganador es: ",ejercicio3())
        ejercicio2(int(input("Please enter a number to evaluate:")))
    elif option == "4":
        print("***** Ejercicio 4 *****")
        ejercicio4()

main()
