matriz = [
    [1, 1, 1, 3],
    [2, 2, 2, 7],
    [3, 3, 3, 9],
    [4, 4, 4, 13]
]


def separar(lista, n):
    if n<= 3:
        fila = lista.pop()
        print(fila)
        n = n + 1
        separar(lista, n)
        sumar_num(fila)
        correccion(fila)
        nueva_matriz(fila)
    else:
        pass


def sumar_num(fila):
    num = sum(fila)
    print(num)
    quitar_error(num, fila)
    return num

def quitar_error(num, fila):
    if num % 2 == 0:
        pass
    else:
        fila.pop(3)
        print(fila)

def correccion(fila):
    if len(fila) == 3:
        num_bien = sum(fila)
        fila.append(num_bien)
        print(fila)
    else: 
        pass

def nueva_matriz(fila):
    matriz.append(fila)
    print(matriz)

separar(matriz, 0)