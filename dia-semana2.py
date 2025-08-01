def dia_da_semana(dia):
    match dia:
        case 1:
            return "segunda"
        case 2:
            return "terça"
        case 3:
            return "quarta"
        case 4:
            return "quinta"
        case 5:
            return "sexta"
        case 6:
            return "sabado"
        case 7:
            return "domingo"


print(dia_da_semana(6))