def extrai_valor(carta:str) -> str:
    
    if (len(carta) == 3):
        return carta[:2]
    
    return carta[0]
    