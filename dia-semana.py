def dia_da_semana(dia):
    match dia:
        case "sábado" | "domingo":
            print("fim de semana")
        case "segunda"|"terça"|"quarta"|"quinta"|"sexta":
            print("dia útil")
        case _:
            print("dia inválido")

print(dia_da_semana("sabado"))