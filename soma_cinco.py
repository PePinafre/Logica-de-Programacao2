'''num1 = float(input("informe um número: "))
num2 = float(input("informe um número: "))
num3 = float(input("informe um número: "))
num4 = float(input("informe um número: "))
num5 = float(input("informe um número: "))

print(f"A soma dos números é {num1+num2+num3+num4+num5}")
'''
soma = 0 

for i in range(5):
    numero = float(input(f"Digite o {i+1}º número: "))
    soma += numero

print("A soma dos numeros é:", soma)
