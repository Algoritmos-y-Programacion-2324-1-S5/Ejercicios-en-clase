def main():
    archivo = open('archivo2.txt','rb')
    datos = archivo.read()
    archivo.close()
    print(datos)

main()