# Imports
import random
from Feedback import feedback
from Computer import computer


def secret():
    passw = []
    while len(passw) < 4:
        passw.append(random.randint(1, 6))
    gok = str(input("Raad 4 getallen tussen de 1 en 6: "))
    gok_list = [int(i) for i in gok]

    while True:
        # tel = 10
        for a in gok_list:
            if a > 6 or a < 1:
                print("Alleen getallen tussen de 1 en 6, raad nogmaals")
                secret()
                break
        if len(gok_list) != 4:
            print("Raad 4 getallen, raad nogmaals")
            secret()
            break
        if gok_list == passw:
            print("GOED GERADEN!")
            break
        elif gok_list != passw:
            # tel -= 1
            # print(feedback(gok_list, passw), "= (wit, zwart)", "\n", tel, "pogingen over")
            print(feedback(gok_list, passw), "= (wit, zwart)")
            secret()
            break

def menu():
    keuze = input("Welkom bij Mastermind! Kies een gamemode. \n[a] Raad de geheime code \n[b] Wees de gamemaster \n")
    if keuze.lower() == "a":
        secret()
    if keuze.lower() == "b":
        computer()
menu()