def maior(a,b,c):

    if a > b and a > c:
        print(f"{a} é maior")

    elif b > a and b > c:
        print(f"{b} é maior")

    elif c > a and c > b:
        print(f"{c} é maior")

    else:
        print("os numeros sao iguais")

maior(5,8,2)

