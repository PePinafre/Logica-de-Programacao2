def recebe_notas(nota):
    if nota >= 7:
        return "Aprovado" 
    elif nota < 7 and nota >= 6:
        return "Recuperação"
    else:
        return "Reprovado"

print(recebe_notas(7)) 
print(recebe_notas(6)) 
print(recebe_notas(5)) 