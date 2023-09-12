# Algoritmo de ordenação por seleção (selection sort)

def executar_selection_sort(lista):
    n = len(lista)

    for i in range(0, n-1):
        min = i
        for j in range(i+1, n):
            if lista[j] < lista[min]:
                min = j
        lista[i], lista[min] = lista[min], lista[i]
    return lista


lista = [10, 8, 7, 3, 2, 1]
executar_selection_sort(lista)