# For
lista = []

for i in range(3):

    # ingreso de datos
    dato_ingreso = input('ingrese numero: ')
    # validacion
    if dato_ingreso.isnumeric():
        lista.append(int(dato_ingreso))
    else:
        print('no es un numero')
        break

print(lista)

# While
