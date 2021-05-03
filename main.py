from tools import * # Importa todas as funções básicas para o jogo
import time
import os
import sys

# Imprimir a mensagem de inicio de jogo e esperar enter
with open(os.path.join(sys.path[0], "message.txt"), 'r') as f:
    print(f.read())

input("\nAperte [Enter] para iniciar o jogo...\n")

# Gerar e Mostrar Baralho
baralho = cria_baralho()

# Vamos começar o jogo
while True:
    # O jogo deve continuar?
    existe_movimentos = possui_movimentos_possiveis(baralho)
    if (existe_movimentos):

        print("Status atual do jogo:\n--------\n")    
        print(mostra_baralho(baralho))

        
        index = faz_pergunta_index(f"Digite a carta que deseja mover (1 - {len(baralho)})", len(baralho))


        
        movimentos = lista_movimentos_possiveis(baralho, index)
        if (not movimentos):
            print("Nenhum movimento é possível com esta carta. Tente novamete:")
            
            # Espera um pouco p o usuário ler
            time.sleep(3)
        
        else:
            print("Você pode empilhar a carta sobre:")
            _cartasMovimento = [baralho[index - x] for x in movimentos]
            mostra_baralho(_cartasMovimento)

            destino = faz_pergunta_index(f"Digite a carta sobre a qual você deseja empilhar {baralho[index]}:\n", len(baralho))
            baralho = empilha(baralho, index, baralho.index(_cartasMovimento[destino]))

    else:
        if (len(baralho) == 1):
            print("Parabéns, você ganhou!")
        
        else:
            print("Você perdeu. Agora a skynet vai dominar o seu PC.")
        
        
        continuar = input("Você gostaria de jogar novamente (s/n)?")
        while (continuar not in ["s", "n"]):
            continuar = input("Digite s ou n?")

        if (continuar == 'n'):
            break
    
        else:
            baralho = cria_baralho()
