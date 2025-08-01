def menu():
    saldo = 10500.0

    while True:
        print("\n Menu: ")
        print("1 - saldo")
        print("2 - deposito")
        print("3 - saque")
        print("0 - sair")

        opcao = input("escolha uma opção")

        match opcao:
            case "1":
                print(f"seu saldo é R$ {saldo:.2f}")
            case "2":
                valor = float(input("digite o valor para depósito: R$"))

                if valor > 0:
                    saldo += valor
                    print(f"depósito de R$ {valor:.2f} realizado com sucesso")
                else:
                    print("valor invalido")

            case "3":
                valor = float(input("digite o valor para saque: R$ "))
                if 0 < valor <= saldo:
                    saldo -= valor
                    print(f"saque de R$ {valor:.2f} realizado com sucesso")
                else:
                    print("saldo insuficiente")
            
            case "0":
                print("saindo, obrigado por usar o sistema")
                break
            case _:
                print("opção invalida. tente novamente")