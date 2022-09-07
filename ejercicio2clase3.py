# MENU que comemos hoy:

monto = 0
while True:
    print('\n')
    print('\t MENU\n')
    print('\t que comemos hoy?')
    print('cuanto tienes hoy?', end='\t')
    monto = int(input())
    if monto < 0:
        print('\n vuelva a intentar')
    elif monto == 0:
        print('\n Anda a laburar')
        print('\t \t adios \n')
        break
    elif monto <= 100:
        print('\n toma mate')
    elif monto <= 500:
        print('\n toco verduritas')
    elif monto <= 1000:
        print('podes elegir el menu', end=' ')
    elif monto > 1000:
        print('menu con bebida y postre?', end=' ')
    