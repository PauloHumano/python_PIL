# Str
a = 'esto eEs uuUna cadena'
print(a, type(a))
print('tiene', len(a), 'caracteres')
c = str(120.34)
print(c, type(c))
print(a[0:4])
print(a[-1:4])
#  METODOS
print(a.lower())
print(a.upper())
print(len(a.split()))
# List

lista_1 = ['un string', 4, 2.5, True, [1, 2, 3], ('a', 'b')]
print(lista_1)
print(type(lista_1))
print(len(lista_1))
print(lista_1[2])
var_uno = lista_1[3]
print(var_uno)
print(type(var_uno))
# Metodos
lista_1.append('lista')
print(lista_1)
print(lista_1.index(('a', 'b')))
lista_1.insert(1, 5)
print(lista_1)
# Diccionario
usuario = {
    'nombre': 'octavio',
    'apellido': 'gomez',
    'edad': 38,
    'hobbies': ['futbol', 'musica'],
    'mascota': False}
print(usuario)
print(usuario['edad'])
print(len(usuario))

print(usuario)
print(usuario.get('puesto', 'no encontrado'))
keys_usuario = list(usuario.keys())
print(usuario.get(keys_usuario[0]))
