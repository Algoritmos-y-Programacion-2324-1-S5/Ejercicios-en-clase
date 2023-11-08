from quicksort import quicksort

def binary_search(lista, value):
    mid = len(lista)//2
    if len(lista) < 2 or lista[mid]== value:
        if lista[mid] == value:
            return value
        else: 
            return None

    if value < lista[mid]:
        return binary_search(lista[0:mid],value)
    elif value < lista[mid]:
        return binary_search(lista[mid+1:],value)

def main():
    lista = [6,8,5,2,1,9,4,3,7] 
    lista = quicksort(lista)
    value = binary_search(lista, int(input("Please enter what do you need: ")))
    print(f"The value {value} is present")
main()