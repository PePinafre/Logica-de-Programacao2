class ContaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.__titular = titular
        self.__saldo = saldo_inicial

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            print(f"Depósito de R${valor} realizado com sucesso")
        else:
            print("Valor de depósito inválido")

    def sacar(self, valor):
        if 0 < valor <=self.__saldo:
            self.__saldo -= valor
            print(f"Saque de R${valor} realizado com sucesso")
        else:
            print("Saldo insuficiente")

    def consultar_saldo(self):
        return self.__saldo
    
    '''Getter | Setter:
    Getter é um metodo usado para obter(ler) o valor de um atributo privado
    de uma classe
    Setter é usado para definir(escrever) ou alterar o valor de um atributo
    privado de uma classe'''

    @property
    def titular(self):
        return self.__titular

   
conta = ContaBancaria("João Lucas", 1000)
print(conta.titular)
print(conta.consultar_saldo())

conta.depositar(500)
print(conta.consultar_saldo())

conta.sacar(200)
print(conta.consultar_saldo())

