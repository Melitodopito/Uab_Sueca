
NAIPES = ('♠', '♦', "♥", '♣')
SIMBOLOS = ("2", "3", "4", "5", "6", "D", "V", "R", "7", "A")
VALORES = (0,2, 3, 4, 10, 11)

class Carta:
    def __init__(self,naipe,simbolo,valor):
        self.naipe = NAIPES[naipe]
        self.simbolo = SIMBOLOS[simbolo]
        self.valor = VALORES[valor]

    def mostrar_carta(self):
        print(self.naipe)
        print(self.simbolo)
        print(self.valor)

class Baralho:
    def __init__(self):
        self.cartas = []

    def iniciar_baralho(self):
        naipe = 0
        for i in range(4):
            simbolo = 0
            valor = 0
            for i in range(10):
                if(i >= 5):
                    valor += 1
                self.cartas.append(Carta(naipe, simbolo, valor))
                simbolo += 1
            naipe += 1

    def mostrar_baralho(self):
        index = 0
        if len(self.cartas) > 0:
            for i in range(len(self.cartas)):
                print(f"|{self.cartas[index].naipe}{self.cartas[index].simbolo}|{self.cartas[index].valor}|")
                index += 1
        else:
            print("\nBaralho Vazio\n")
