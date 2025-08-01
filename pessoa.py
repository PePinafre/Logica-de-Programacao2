class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.__idade = idade

    def mostrar_idade(self):
        print(f"Idade: {self.__idade}")


p = Pessoa("Antonio", 18)
print(p.nome)
p.mostrar_idade()

        