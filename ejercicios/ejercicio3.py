x = range(-20, 51)
lista = list(x)
print(lista)
lista1 = []
lista2 = []

def lista_1(lista, n):
    if n < len(lista):
        if 0 <= lista[n] <= 10:
                lista1.append(lista[n])
                lista_1(lista,n+1)
        else:
            lista_1(lista, n+2)
    else:
        pass

def lista_2(lista, n):
    if n < len(lista):
        if -10 <= lista[n] <= 0:
                lista2.append(lista[n])
                lista_2(lista,n +1)
        else:
            lista_2(lista, n+2)
    else:
        pass

lista_1(lista, 0)
lista_2(lista, 0)
print(lista1)
print(lista2)
