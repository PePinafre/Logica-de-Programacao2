def remove_duplicatas(lista):
    nova_lista = []
    vistos = set()

    for item in lista:
        if item not in vistos:
            nova_lista.append(item)
            vistos.add(item)
    return nova_lista

lista = [1,1,2,3,4,5,6,7,8,9,2,3,4,5,6,7,8,9]
resultado = remove_duplicatas(lista)
print(resultado)