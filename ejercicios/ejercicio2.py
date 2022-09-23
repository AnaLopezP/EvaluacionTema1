cadena = str(input())

def cadena_a_lista(cadena):
    lista = list(cadena)
    print(lista)
    solucion = lista_longitud(lista)
    print(solucion)

def lista_longitud(lista):
    if 3 <= len(lista) <= 10:
        return True
    else:
        return False

cadena_a_lista(cadena)