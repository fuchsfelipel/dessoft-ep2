import random

def cria_baralho():
    naipes = ["♠", "♥", "♦", "♣"]
    letras = [str(x + 2) for x in range(9)]
    letras.extend(["J", "Q", "K", "A"])
    
    cartas = []

    # Gera as cartas
    for letra in letras:
        for naipe in naipes:
            cartas.append(letra + naipe)

    random.shuffle(cartas)

    return(cartas)

def empilha(baralho:int, origem:int, destino:int) -> list:
    # Usar o pop na associação certifica de
    # que os indíces não se percam entre uma
    # operação e outra
    baralho[destino] = baralho.pop(origem)
    return(baralho)

def extrai_naipe(carta:str) -> str:
    return carta[-1]

def extrai_valor(carta:str) -> str:
    
    if (len(carta) == 3):
        return carta[:2]
    
    return carta[0]
    
def lista_movimentos_possiveis(baralho:list, index:int) -> list:
    valores = [extrai_valor(carta) for carta in baralho]
    naipes = [extrai_naipe(carta) for carta in baralho]

    movimentos = []

    if (index!= 0 and (naipes[index] == naipes[index - 1] or valores[index] == valores[index - 1])):
        movimentos.append(1)
    
    if (index >= 3 and (naipes[index] == naipes[index - 3] or valores[index] == valores[index - 3])):
        movimentos.append(3)
    
    return movimentos

def possui_movimentos_possiveis(baralho:list) -> bool:
    for i in range(len(baralho)):
        print(i)
        print(lista_movimentos_possiveis(baralho, i))
        
        if lista_movimentos_possiveis(baralho, i):
            return True

    return False


def mostra_baralho(baralho:list):
    for carta in baralho:
        print(str(baralho.index(carta) + 1) + ". " + carta) 
