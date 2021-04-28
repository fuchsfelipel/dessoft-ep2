from tools import * # Importa todas as funções básicas para o jogo

# Imprimir a mensagem de inicio de jogo e esperar enter
with open("message.txt", 'r') as f:
    print(f.read())

input("\nAperte [Enter] para iniciar o jogo...\n")

# Gerar e Mostrar Baralho
baralho = cria_baralho()
mostra_baralho(baralho)