from cartas import Carta,Baralho
from jogo import Jogo



print("Bem vindo ao Jogo da Sueca Compadre!")


sueca_is_on = True

while sueca_is_on:
    print("\nO que deseja Fazer?")
    print("1: Iniciar Jogo")
    print("2: Mostrar Jogador")
    opcao = int(input())

    # Iniciar Jogo
    if opcao == 1:

        #Iniciar Baralho
        my_baralho = Baralho()
        my_baralho.iniciar_baralho()
        #Iniciar Jogo
        my_game = Jogo(my_baralho)
        my_game.defenir_jopadores()
        my_game.servir(my_baralho)
        print(f"O Trunfo do jogo é {my_game.trunfo}")



        for ronda in range(10):
            my_game.jogar_ronda()

        my_game.contar_pontos()


    #Mostrar Jogador
    if opcao == 2:
        jogador_para_ver = str(input(f"Que Jogador pretende ver? Por favor escreva o seu nome:"))
        print("\n")

        for jogador in my_game.jogadores:
            if jogador.nome == jogador_para_ver:
                jogador.mostrar_jogador()
                break
        else:
            print("Jogador não encontrado.")




