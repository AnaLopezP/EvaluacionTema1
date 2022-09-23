from ast import Num


matriz = [
    [1, 1, 1, 3]
    [2, 2, 2, 7]
    [3, 3, 3, 9]
    [4, 4, 4, 13]
]


def separar(lista):
    n = 0
    fila = lista.pop()
    n = n + 1
    print(fila)
    if n <= 3:
        separar(lista)
    else:
        pass

separar(matriz)