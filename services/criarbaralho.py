def cria_baralho():
    naipes = ["♠", "♥", "♦", "♣"]
    letras = [str(x + 2) for x in range(9)]
    letras.extend(["J", "Q", "K", "A"])
    
    cartas = []

    # Gera as cartas
    for letra in letras:
        for naipe in naipes:
            cartas.append(letra + naipe)

    return(cartas)