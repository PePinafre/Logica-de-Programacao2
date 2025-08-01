'''def analisa_salarios(*salarios):
    if not salarios:
        print("Nenhum salário foi fornecido.")
        return

    media = sum(salarios) / len(salarios)
    menor = min(salarios)
    maior = max(salarios)
    acima_da_media = [s for s in salarios if s > media]
    total_pago = sum(salarios)

    print(f"Média salarial: R${media:.2f}")
    print(f"Menor salário: R${menor:.2f}")
    print(f"Maior salário: R${maior:.2f}")
    print(f"Colaboradores acima da média: {len(acima_da_media)}")
    print(f"Total pago em salários: R${total_pago:.2f}")

# Exemplo de uso:
analisa_salarios(2500.0, 3200.0, 4000.0, 1800.0, 2200.0)'''

def analisa_salarios(*salarios):
    if not salarios:
        return "nenhum salario fornecido"
    
    media_salarial = sum(salarios)/ len(salarios)

    menor_salario = min(salarios)
    maior_salario = max(salarios)

    acima_media = 0
    for salario in salarios:
        if salario > media_salarial:
            acima_media +=1
    
    total_pago = sum(salarios)

    return{
        "media_salarial": media_salarial,
        "menor_salario" : menor_salario,
        "maior_salario" : maior_salario,
        "colaboradores_acima_media" : acima_media,
        "total_pago" : total_pago

    }

print(analisa_salarios(2500.0, 3200.0, 4000.0, 1800.0, 2200.0))
