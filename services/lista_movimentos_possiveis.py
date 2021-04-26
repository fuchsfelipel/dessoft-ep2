import criarbaralho
import extrainaipe
import extraivalor

def lista_movimentos_possiveis(baralho:list, index:int) -> list:
    valores = [extrai_valor(carta) for carta in baralho]
    naipes = [extrai_naipe(carta) for carta in baralho]
    
lista_movimentos_possiveis(criar_baralho(), 0)
