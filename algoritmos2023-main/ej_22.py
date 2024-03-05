def usar_la_fuerza(mochila, objetos_sacados=0):
    if not mochila:
        return 0
    elif mochila[0] == "sable de luz":
        return objetos_sacados
    else:
        return usar_la_fuerza(mochila[1:], objetos_sacados + 1)
