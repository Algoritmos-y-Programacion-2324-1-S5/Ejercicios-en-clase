def main():
    lista = [6,8,5,2,1,9,4,3,7] # 1
    position = 0 #1
    while position < len(lista): #n
        temp = position #n
        while position > 0 and temp > 0 and lista[temp] < lista[temp-1]: #n2
            aux = lista[temp] #n2
            lista[temp] = lista[temp-1]#n2
            lista[temp-1] = aux#n2
            temp -= 1#n2
        position += 1#n
    #2+3n+5n2 => O(n2)
    print(lista)

main()