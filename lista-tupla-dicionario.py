#Lista: Coleção ordenada e mutável de elemntos. Pode ser modificada
#consigo excluir, adicionar e atualizar uma lista
frutas = ["maçã","banana","laranja"]
print(frutas)

#Adiciona item na lista
frutas.append("uva")
print(frutas)

#tupla: coleção ordenada, mas IMUTÁVEL(não pode ser alterada após criada)
coordenadas = (10.0, 20.0)
print(coordenadas)

#dicionário: coleção não ordenada de pares chave-valor
aluno = {
    "nome": "Mauro",
    "idade": 25,
    "apelido":"An, Oruam",
    "curso": "An, Cardique"
}
print(aluno)
print(aluno["nome"])
aluno["idade"] = 21
print (aluno)
