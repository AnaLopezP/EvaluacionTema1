x = range(-20, 51)
lista = list(x)
print(lista)
lista1 = []
lista2 = []
lista3 = []
lista4 = []
lista5 = []

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

def lista_3(lista, n):
    if n < len(lista):
        if lista[n]%2 == 0:
            if 0 <= lista[n] <= 20:
                lista3.append(lista[n])
                lista_3(lista, n+1)
            else:
                lista_3(lista, n+2)
        else:
            lista_3(lista, n+1)
    else:
        pass

def lista_4(lista, n):
    if n < len(lista):
        if lista[n]%2 == 1:
            if -20 <= lista[n] <= 0:
                lista4.append(lista[n])
                lista_4(lista, n+1)
            else:
                lista_4(lista, n+2)
        else:
            lista_4(lista, n+1)
    else:
        pass

def lista_5(lista, n):
    if n < len(lista):
        if lista[n]%5 == 0:
            if 0 <= lista[n] <= 50:
                lista5.append(lista[n])
                lista_5(lista, n+1)
            else:
                lista_5(lista, n+2)
        else:
            lista_5(lista, n+1)
    else:
        pass


lista_1(lista, 0)
lista_2(lista, 0)
lista_3(lista, 0)
lista_4(lista, 0)
lista_5(lista, 0)
print(lista1)
print(lista2)
print(lista3)
print(lista4)
print(lista5)
