#for: usamos para repetir o código com um número CONHECIDO E DEFINIDO de vezes
for i in range (1,6): #range: repetição de 1 a 6 = índice vetor
    print(i)

alunos = ["Melquisedeque", "Rebeca", "Sara", "Abraão", "Paulo", "Noé"]

for aluno in alunos: #em: dentro
    print(aluno) #printa o elemento sozinho

print(alunos)

#while: usado para repetir o código enquanto a condição for verdadeira
#não sabemos quantas vezes irá repetir
i = 10

while i<=50:
    print(i)
    i += 10