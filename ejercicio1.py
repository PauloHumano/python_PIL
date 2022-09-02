# crear variables
a = float(2.4)
b = float(-3.21)
c = float(47.8)
# generar diccionario
d = [['a',a],
    ['b',b],
    ['c',c]]
# dar formato a print
print('{:<5} {:<5} {:<5}'.format('a','b','c'))
def new_func(v):
    a, b, c = v
    return a,b,c

for v in d:
    a, b, c = new_func(v)
print('{:<5} {:<5} {:<5}'.format(a, b, c))
