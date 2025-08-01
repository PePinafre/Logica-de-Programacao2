class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos")

pessoa1 = Pessoa("Ana", 25)
pessoa2 = Pessoa("Thais", 27)
pessoa3 = Pessoa("Fernando", 18)

pessoa1.apresentar()
pessoa2.apresentar()
pessoa3.apresentar()