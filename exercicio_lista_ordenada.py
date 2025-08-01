def ordenar_lista(*numeros):
    if not numeros:
        return "nenhum numero fornecido"
    
    ordenada = sorted(numeros)
    print(ordenada)

ordenar_lista(6,5,4,8,2,22,15,3,25)