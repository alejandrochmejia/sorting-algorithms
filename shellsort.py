def shellsort(lista):
    n = len(lista)
    gap = n // 2  # Inicialmente, el gap es la mitad del tamaño de la lista

    while gap > 0:
        for i in range(gap, n):
            temp = lista[i]
            j = i
            # Realiza una comparación de elementos separados por 'gap' y los intercambia si es necesario
            while j >= gap and lista[j - gap] > temp:
                lista[j] = lista[j - gap]
                j -= gap
            lista[j] = temp
        gap //= 2  # Reduce el gap para la siguiente iteración

    return lista

# Ejemplo de uso:
lista = [3,6,8,10,1,2,1]
lista = shellsort(lista)
print(lista)
