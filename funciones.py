# funcion 1

# Nombre
# Argumento
# Codigo
# Retotno

def sumar(a, b):
    resultado = a + b

    return resultado


resultado_suma = sumar(2, 3)
print(sumar(2, 3))
print(resultado_suma)

# funcion 2


def resta():
    resultado = 2 - 3

    return resultado


print(resta())

# funcion 3


def saludo(cantidad_saludos):
    """_summary_ ordena los nombres en formato lista


    Returns:
        _type_: _description_
    """
    lista_nombres = []

    # bucle de ingreso de nombres

    for i in range(cantidad_saludos):

        nombre = input('ingrese nombre: ')
        print('hola', nombre)
        print('hola', nombre)
        lista_nombres.append(nombre)

    return lista_nombres


def orden(lista, sentido):
    """ ordena los nombres ingresados segun se solicite
    Args: lista (list): lista generica
    sentido (bool): definir si se ordena de mayor a menor o de menor  a mayor
    """

    lista.sort(reverse=sentido)

    return lista


nombres = saludo(int(input('ingrese la cantidad de saludos a efectuar: ')))

print(orden(nombres, True))
