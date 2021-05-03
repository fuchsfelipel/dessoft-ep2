from tools import * # Importa todas as funções básicas para o jogo
import time
# Imprimir a mensagem de inicio de jogo e esperar enter
with open("message.txt", 'r') as f:
    print(f.read())

input("\nAperte [Enter] para iniciar o jogo...\n")

# Define uma jogada
"Você gostaria de jogar novamente (s/n)?"



# Gerar e Mostrar Baralho
baralho = cria_baralho()

while True:
    print("Status atual do jogo:\n--------\n")    
    print(mostra_baralho(baralho))

    index = int(input(f"Digite a carta que deseja mover (1 - {len(baralho)})")) - 1

    # O jogo deve continuar?
    if (possui_movimentos_possiveis(baralho)):
        movimentos = lista_movimentos_possiveis(baralho, index)
        if (not movimentos):
            print("Nenhum movimento é possível com esta carta. Tente novamete:")
            
            # Espera um pouco p o usuário ler
            time.sleep(3)
        
        else:
            print("Você pode embilhar a carta sobre:")
            _cartasMovimento = [baralho[index - x] for x in movimentos]
            mostra_baralho(_cartasMovimento)
            destino = int(input(f"Digite a carta sobre a qual você deseja empilhar {baralho[index]}:\n")) - 1
            baralho = empilha(baralho, index, baralho.index(_cartasMovimento[destino]))

    else:
        if (len(baralho) == 1):
            print("Parabéns, você ganhou!")
        
        else:
            print("Você perdeu. Agora a skynet vai dominar o seu PC.")
        
        if (input("Você gostaria de jogar novamente (s/n)?") == "n"):
            break
    
        else:
            baralho = cria_baralho()
