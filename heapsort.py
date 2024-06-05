def heapify(lista, n, i):
    mayor = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and lista[i] < lista[l]:
        mayor = l

    if r < n and lista[mayor] < lista[r]:
        mayor = r

    if mayor!= i:
        lista[i], lista[mayor] = lista[mayor], lista[i]
        heapify(lista, n, mayor)

def heapsort(lista):
    n = len(lista)

    # Construimos el montículo
    for i in range(n // 2 - 1, -1, -1):
        heapify(lista, n, i)

    # Desapilamos los elementos del montículo y ordenamos el arreglo
    for i in range(n - 1, 0, -1):
        lista[i], lista[0] = lista[0], lista[i]
        heapify(lista, i, 0)
    return lista

# Ejemplo de uso
lista = [3,6,8,10,1,2,1]
lista = heapsort(lista)
print(lista)