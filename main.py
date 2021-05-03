from tools import * # Importa todas as funções básicas para o jogo

# Imprimir a mensagem de inicio de jogo e esperar enter
with open("message.txt", 'r') as f:
    print(f.read())

input("\nAperte [Enter] para iniciar o jogo...\n")

# Gerar e Mostrar Baralho
baralho = cria_baralho()

# Define uma jogada
def jogar():
    statusJogo = True
    
    # Mostrar info do baralho p usuário
    print("Status atual do jogo:\n--------\n")
    print(mostra_baralho(baralho))

    baralho_atual = baralho
    while statusJogo:
        index = int(input(f"Digite a carta que deseja mover (1 - {len(baralho)})")) - 1
        statusJogo, baralho_atual = fazJogada(baralho_atual, index)

# Jogar
while True:
    jogar()
    if (input("Você gostaria de jogar novamente (s/n)?") == 'n'):
        break 
