def empilha(baralho:int, origem:int, destino:int) -> list:
    # Usar o pop na associação certifica de
    # que os indíces não se percam entre uma
    # operação e outra
    baralho[destino] = baralho.pop(origem)
    return(baralho)
