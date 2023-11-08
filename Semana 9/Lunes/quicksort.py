def main(): 
    lista = [6,5,3,1,8,7,2,4]
    print(lista)
    lista2 = quicksort(lista)
    print(lista2)


def quicksort(lista):
    if len(lista) < 2:
        return lista
    menor, pivote, mayor = partition(lista)

    return quicksort(menor) + [pivote] + quicksort(mayor)


def partition(lista):
    menor = []
    mayor = []
    pivote = lista[0]
    for i in range(len(lista)):
        if lista[i] < pivote:
            menor.append(lista[i])
        elif lista[i] > pivote:
            mayor.append(lista[i])
    return menor, pivote, mayor

main()