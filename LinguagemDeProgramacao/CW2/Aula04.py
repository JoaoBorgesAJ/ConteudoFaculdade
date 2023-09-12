# Busca Binaria

def busca_binaria(lista, elemento):
    minimo = 0
    maximo = len(lista)-1
    encontrado = False

    while minimo <= maximo and not encontrado:
        meio_lista = (minimo + maximo) //2
        if lista[meio_lista] == elemento:
            encontrado = True
        else:
            if elemento < lista[meio_lista]:
                maximo = meio_lista-1
            else:
                minimo = meio_lista+1
    return encontrado
testelista = [1, 2, 8, 10, 13, 15, 18, 20]
print(busca_binaria(testelista, 5))
print(busca_binaria(testelista, 15))
