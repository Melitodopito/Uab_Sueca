import random

from jogadores import Jogador
from cartas import Carta
class Jogo:
    def __init__(self, baralho):
        # Geral
        self.baralho = baralho
        self.jogadores = []
        self.pontuacoes = []
        self.trunfo = ""

        # Ronda
        self.ronda = 1
        self.jogadores_de_ronda = []
        self.index_jogador_atual = 0
        self.cartas_na_ronda = []
        self.naipe_escolhido = ""

    def defenir_jopadores(self):
        nome_player = input("Como se chama o Jogador?")
        equipa = 1
        jogador = Jogador(nome_player, equipa)
        self.jogadores.append(jogador)
        for i in range(3):
            if i % 2 == 0:
                nome = str(input("Como se chamara o teu adversario?"))
                equipa = 2
            else:
                nome = str(input("Como se chamara o teu companheiro?"))
                equipa = 1

            jogador = Jogador(nome,equipa)
            self.jogadores.append(jogador)

    def servir(self, baralho):
        for jogador in self.jogadores:
            for i in range(10):
                carta_escolhida = random.choice(baralho.cartas)
                jogador.cartas.append(carta_escolhida)
                baralho.cartas.remove(carta_escolhida)
        self.trunfo = self.jogadores[0].cartas[0].naipe

        for jogador in self.jogadores:
            jogador.cartas = sorted(jogador.cartas, key=lambda carta: (carta.naipe, carta.simbolo))


    def jogar_ronda(self):
        print(f"Ronda {self.ronda}")


        while len(self.cartas_na_ronda) < 4:
            # Atualizar o jogador atual
            jogador_a_jogar = self.jogadores[self.index_jogador_atual]
            print(f"É a vez do {jogador_a_jogar.nome} jogar!")

            if self.index_jogador_atual == 0:
                self.jogador_joga()
                self.index_jogador_atual = (self.index_jogador_atual + 1) % len(self.jogadores)
            else:
                self.cpu_joga(self.index_jogador_atual)
                self.index_jogador_atual = (self.index_jogador_atual + 1) % len(self.jogadores)

            # Establecer o Naipe da ronda
            if len(self.cartas_na_ronda) == 1:
                self.naipe_escolhido = self.cartas_na_ronda[0].naipe

        print("Cartas na Ronda:",end=" ")
        for carta in self.cartas_na_ronda:
            print(f"{carta.simbolo}{carta.naipe}",end = " ")
        print("\n")

        self.escolha_de_vencedor()

        self.ronda += 1
        self.cartas_na_ronda = []
        self.jogadores_de_ronda = []



    def mostrar_cartas_jogador(self):
        print("Tu tens na mão:")
        for index, carta in enumerate(self.jogadores[0].cartas):
            print(f"{index} --> |{carta.naipe}{carta.simbolo}|", end=" ")
        print("\n")

    def jogador_joga(self):
        print("Seleciona uma carta:")
        self.mostrar_cartas_jogador()
        carta_jogada = False
        while not carta_jogada:
            try:
                carta_a_tirar = int(input("Que Carta vais jogar?"))
                self.cartas_na_ronda.append(self.jogadores[0].cartas.pop(carta_a_tirar))
                self.jogadores_de_ronda.append(self.jogadores[0].nome)
                carta_jogada = True
            except:
                print("Escolhe uma carta válida!")



    def cpu_joga(self, index):

        cartas_com_naipe_equivalente = []
        trunfos = []

        if len(self.cartas_na_ronda) == 0:
            carta_a_tirar = random.choice(self.jogadores[index].cartas)
            print(f"\nCarta jogada {carta_a_tirar.simbolo}{carta_a_tirar.naipe} ")
            self.cartas_na_ronda.append(carta_a_tirar)
            self.jogadores[index].cartas.remove(carta_a_tirar)
        else:

            for carta in self.jogadores[index].cartas:
                if carta.naipe == self.naipe_escolhido:
                    cartas_com_naipe_equivalente.append(carta)
                elif carta.naipe == self.trunfo:
                    trunfos.append(carta)

            self.escolha_de_carta(cartas_com_naipe_equivalente,trunfos,self.index_jogador_atual)

        # Escolha da carta em em si
        self.jogadores_de_ronda.append(self.jogadores[self.index_jogador_atual].nome)
        print(f"\nO {self.jogadores[index].nome} Joga!")




    def escolha_de_carta(self,cartas_com_naipe_equivalente,trunfos,index):

        # Sem cartas com o mesmo naipe e sem trunfos
        if len(cartas_com_naipe_equivalente) == 0 and len(trunfos) == 0:
            carta_a_tirar = random.choice(self.jogadores[index].cartas)
            print(f"\nCarta jogada {carta_a_tirar.simbolo}{carta_a_tirar.naipe} ")
            self.cartas_na_ronda.append(carta_a_tirar)

        # Sem cartas com o mesmo naipe
        elif len(cartas_com_naipe_equivalente) == 0:
            carta_a_tirar = random.choice(trunfos)
            print(f"\nCarta jogada {carta_a_tirar.simbolo}{carta_a_tirar.naipe} ")
            self.cartas_na_ronda.append(carta_a_tirar)
        else:
            carta_a_tirar = random.choice(cartas_com_naipe_equivalente)
            print(f"\nCarta jogada {carta_a_tirar.simbolo}{carta_a_tirar.naipe} ")
            self.cartas_na_ronda.append(carta_a_tirar)

        self.jogadores[index].cartas.remove(carta_a_tirar)


    def escolha_de_vencedor(self):
        pontuacao_da_ronda = 0
        trunfos_na_ronda = 0
        carta_vencedora = Carta(0,0,0)

        for carta in self.cartas_na_ronda:
            pontuacao_da_ronda += carta.valor
            if carta.naipe == self.trunfo and trunfos_na_ronda == 0:
                trunfos_na_ronda += 1
                carta_vencedora = carta
            elif carta.valor > carta_vencedora.valor and carta.naipe == self.naipe_escolhido and trunfos_na_ronda == 0:
                carta_vencedora = carta
            elif carta.valor > carta_vencedora.valor and carta.naipe == self.trunfo:
                trunfos_na_ronda += 1
                carta_vencedora = carta

        print(self.jogadores_de_ronda)
        index_carta_vencedora= self.cartas_na_ronda.index(carta_vencedora)
        jogador_vencedor = self.jogadores_de_ronda[index_carta_vencedora]
        print(jogador_vencedor)
        print(f" CARTA VENCEDORA: |{carta_vencedora.naipe}{carta_vencedora.simbolo}|{carta_vencedora.valor}|")

        for jogador in self.jogadores:
            if jogador_vencedor == jogador.nome:
                jogador.pontuacao += pontuacao_da_ronda
                print(f"O JOGADOR {jogador.nome} tem {jogador.pontuacao}")

                #Defenir quem começa a nova ronda
                index_vencedor_ronda = self.jogadores.index(jogador)
                self.index_jogador_atual = index_vencedor_ronda





    def contar_pontos(self):
        pontos_equipa_1 = 0
        pontos_equipa_2 = 0
        equipa_vencedora = 0
        for jogador in self.jogadores:
            if self.jogadores.index(jogador) % 2 == 0:
                pontos_equipa_1 += jogador.pontuacao
            else:
                pontos_equipa_2 += jogador.pontuacao
        if pontos_equipa_2 > pontos_equipa_1:
            equipa_vencedora = 2
        else:
            equipa_vencedora = 1

        print(f" A equipa 1 fez {pontos_equipa_1}, enquanto a equipa 2 fez {pontos_equipa_2}, portanto a equipa {equipa_vencedora} venceu! PARABENS!")




