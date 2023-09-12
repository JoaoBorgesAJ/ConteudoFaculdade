# Algoritmo de Ordenação por inserção (Insertion Sort)

def executar_insertion_sort(lista):
    n = len(lista)
    for i in range(1, n):
        valor_inserir = lista[i]
        j = i - 1

        while j >= 0 and lista[j] > valor_inserir:
            lista [j + 1] = lista[j]
            j -= 1
        lista[j + 1] = valor_inserir
    return lista


lista = [10, 8, 7, 3, 2, 1]
executar_insertion_sort(lista)