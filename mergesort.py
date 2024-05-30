def mergesort(lista):
    if len(lista) <= 1:
        return lista
    else:
        mitad = len(lista)//2
        izquierda = lista[:mitad]
        derecha = lista[mitad:]
        izquierda = mergesort(izquierda)
        derecha = mergesort(derecha)
        return merge(izquierda, derecha)

def merge(izquierda, derecha):
    resultado = []
    i = 0
    j = 0 
    while i < len(izquierda) and j < len(derecha):
        if izquierda[i] <= derecha[j]:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1
    resultado += izquierda[i:]
    resultado += derecha[j:]
    return resultado

lista = [3,6,8,10,1,2,1]
lista = mergesort(lista)
print(lista)