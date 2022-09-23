x = range(-20, 51)
lista = list(x)
print(lista)
lista1 = []

def lista_1(lista, n):
    if n < len(lista):
        if 0 <= lista[n] <= 10:
                a = lista.pop(n)
                lista1.append(a)
                lista_1(lista,n)
        else:
            lista_1(lista, n+1)
    else:
        pass

lista_1(lista, 0)
print(lista1)