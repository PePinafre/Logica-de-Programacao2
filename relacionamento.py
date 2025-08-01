'''Crie um sistema simples para registrar e exibir
relacionamentos amorosos entre pessoas'''

class Pessoa:
    def __init__(self, nome):  # init: inicializar um objeto
        self.nome = nome
        self.parceiros = []

    def adicionar_parceiro(self, relacionamento):
        self.parceiros.append(relacionamento)

    def mostrar_parceiros(self):
        if not self.parceiros:
            print(f"{self.nome} não possui parceiros registrados.")
        else:
            print(f"Parceiros amorosos de {self.nome}:")
            for rel in self.parceiros:
                if rel.pessoa1 == self:
                    parceiro = rel.pessoa2
                else:
                    parceiro = rel.pessoa1
                print(f" - {parceiro.nome}, desde {rel.ano_inicio}") 
                
class relacionamento:
    def __init__(self, pessoa1, pessoa2, ano_inicio): #self: relacionado ao objeto que esta sendo criado/manipulado
        self.pessoa1 = pessoa1
        self.pessoa2 = pessoa2
        self.ano_inicio = ano_inicio
        
    def mostrar_informacao(self):
        print(f"{self.pessoa1.nome} e {self.pessoa2.nome} estão juntos desde {self.ano_inicio}")

#criando pessoas
ana = Pessoa("ana")
bruno = Pessoa("bruno")
carla = Pessoa    ("Carla")
daniel = Pessoa("Daniel")
elisa = Pessoa("Elisa")
felipe = Pessoa("Felipe")
gabriela = Pessoa("Gabriela")
henrique = Pessoa("Henrique")
Brino = Pessoa("brino")
felca = Pessoa("felca")

#criando relacionamentos
relacionamento1 = relacionamento(ana, felca, 2017 )
relacionamento2 = relacionamento(bruno, carla, 2018)
relacionamento3 = relacionamento(daniel, elisa, 2019)
relacionamento4 = relacionamento(felipe, gabriela, 2020)
relacionamento5 = relacionamento(henrique, ana, 2021)
relacionamento6 = relacionamento(Brino, felca, 2022)
relacionamento7 = relacionamento(carla, daniel, 2016)
relacionamento8 = relacionamento(elisa, henrique, 2015)
relacionamento9 = relacionamento(gabriela, Brino, 2023)
relacionamento10 = relacionamento(felipe, ana, 2024)

#associar relacionamento a pessoas
ana.adicionar_parceiro(relacionamento1)
felca.adicionar_parceiro(relacionamento1) 

bruno.adicionar_parceiro(relacionamento2)
carla.adicionar_parceiro(relacionamento2)

daniel.adicionar_parceiro(relacionamento3)
elisa.adicionar_parceiro(relacionamento3)

felipe.adicionar_parceiro(relacionamento4)
gabriela.adicionar_parceiro(relacionamento4)

henrique.adicionar_parceiro(relacionamento5)
ana.adicionar_parceiro(relacionamento5)

Brino.adicionar_parceiro(relacionamento6)
felca.adicionar_parceiro(relacionamento6)

carla.adicionar_parceiro(relacionamento7)
daniel.adicionar_parceiro(relacionamento7)

elisa.adicionar_parceiro(relacionamento8)
henrique.adicionar_parceiro(relacionamento8)

gabriela.adicionar_parceiro(relacionamento9)
Brino.adicionar_parceiro(relacionamento9)

felipe.adicionar_parceiro(relacionamento10)
ana.adicionar_parceiro(relacionamento10)

#exibir
ana.mostrar_parceiros()