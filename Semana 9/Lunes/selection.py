def main():
    lista = [6,8,5,2,1,9,4,3,7]#1
    position = 0#1
    while position < len(lista):#n
        temp = position+1#n
        min_index = position#n
        while temp < len(lista):#n2
            if lista[temp] < lista[min_index]:#n2
                min_index = temp#n2
            temp+=1#n2
        aux = lista[position]#n
        lista[position] = lista[min_index]#n
        lista[min_index] = aux#n
        position += 1#n
    #2+7n+4n2 => O(n2)
    print(lista)

main()