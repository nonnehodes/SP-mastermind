def feedback(gok_list, passw):
    wit = wit_pin(gok_list, passw)
    zwart = zwart_pin(gok_list, passw)
    return wit, zwart


def wit_pin(gok_list, passw):
    wit = 0
    wit_list = passw[:]
    for w in gok_list:
        if w in wit_list:
            wit_list.remove(w)
            wit = wit + 1
    return wit


def zwart_pin(gok_list, passw):
    zwart = 0
    zwart_list = passw[:]
    teller = 0
    for z in gok_list:
        if z == zwart_list[teller]:
            zwart += 1
        teller += 1
    return zwart