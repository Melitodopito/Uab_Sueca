class Jogador:
    def __init__(self,nome,equipa):
        self.cartas = []
        self.nome = nome
        self.pontuacao = 0
        self.equipa_do_jogador = equipa


    def mostrar_jogador(self):
        print("Mão:", end=" ")
        for i in range(len(self.cartas)):
            print(f"|{self.cartas[i].naipe}{self.cartas[i].simbolo}|{self.cartas[i].valor}|", end=" ")
        print("\n")
        print(f"Equipa: {self.equipa_do_jogador}")
        print(f"Pontuação: {self.pontuacao}")