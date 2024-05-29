def quicksort(lista):
    if len(lista) <= 1:
        return lista
    else:
        pivote = lista[0]
        menores = [x for x in lista[1:] if x <= pivote]
        mayores = [x for x in lista[1:] if x > pivote]
        return quicksort(menores) + [pivote] + quicksort(mayores)
    
lista = [3,6,8,10,1,2,1]
lista = quicksort(lista)
print(lista)