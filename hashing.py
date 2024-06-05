def hashing(lista):
    if len(lista) == 0:
        return lista

    # Encontrar el valor máximo y mínimo en la lista
    minimo = min(lista)
    maximo = max(lista)

    # Calcular el número de cubos (buckets)
    cant = len(lista)
    buckets = [[] for _ in range(cant)]

    # Distribuir los elementos en los cubos
    for num in lista:
        # Calcula el índice del cubo
        index = int((num - minimo) / (maximo - minimo + 1) * cant)
        buckets[index].append(num)

    # Ordenar individualmente cada cubo y concatenarlos
    ordenada = []
    for bucket in buckets:
        ordenada.extend(sorted(bucket))

    return ordenada

# Ejemplo de uso:
lista = [3,6,8,10,1,2,1]
lista = hashing(lista)
print(lista)
