num1 = float(input("informe um número: "))
num2 = float(input("informe um número: "))
num3 = float(input("informe um número: "))

if num1 > num2 and num1 > num3:
    print(f"{num1} é maior")
elif num2 > num1 and num2 > num3:
    print(f"{num2} é maior")
elif num3 > num1 and num3 > num2:
    print(f"{num3} é maior")
else:
    print("os numeros sao iguais")