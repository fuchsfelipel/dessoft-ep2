import extrainaipe
import extraivalor

def lista_movimentos_possiveis(baralho:list, index:int) -> list:
    valores = [extrai_valor(carta) for carta in baralho]
    naipes = [extrai_naipe(carta) for carta in baralho]

    movimentos = []

    if (index!= 0 and (naipes[index] == naipes[index - 1] or valores[index] == valores[index - 1])):
        movimentos.Append(1)
    
    if (index >= 3 and (naipes[index] == naipes[index - 3] or valores[index] == valores[index - 3])):
        movimentos.Append(3)
    
    return movimentos
