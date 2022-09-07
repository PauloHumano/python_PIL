# MENU con while true:

opcion = 0
while True:
    print('\n')
    print('\t MENU\n')
    print('\t 1.deposito')
    print('\t 2.extraccion')
    print('\t 3.transferencia')
    print('\t 4.salir')
    print('ingrese opcion', end='\t')
    opcion = int(input())
    if opcion > 4:
        print('\n vuelva a intentar')
    elif opcion == 0:
        print('\n vuelva a intentar')
    elif opcion == 1:
        print('ingrese monto deposito', end=' ')
        monto = input()
    elif opcion == 2:
        print('ingrese monto extraccion', end=' ')
        monto = input()
    elif opcion == 3:
        print('ingrese monto transferencia', end=' ')
        monto = input()
    elif opcion == 4:
        print('\t \t adios')
        break
