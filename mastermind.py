# Imports
import random
import time

# De computer raadt
def secret_input():
    password = []
    while len(password) < 4:
        secret = int(input("Geef een getal tussen de 0 en 6: "))
        if secret > 6:
            print("Onder de 7 graag.")
        elif secret <= 6:
            password.append(secret)
    print("Jouw geheime code is", password)
    time.sleep(2)
    print("De computer gaat nu beginnen met raden")


def computer():
    password = []
    secret = input("Maak een geheime code aan met 4 getallen tussen de 1 en 6: ")
    secret_list = [int(i) for i in secret]
    for x in secret_list:
        if x > 6 or x < 1:
            secret = input("Maak een geheime code aan met 4 getallen tussen de 0 en 6: ")
            print("Gebruik alleen getallen onder de 7.\n", secret)
    if len(secret_list) != 4:
        secret = input("Maak een geheime code aan met 4 getallen tussen de 0 en 6: ")
        print("Maak een 4 cijferige code aan.\n", secret)
    print(secret_list)




# De speler raadt
passw = []
while len(passw) < 4:
    passw.append(random.randint(1, 6))
def secret():
    gok = str(input("Raad 4 getallen tussen de 1 en 6: "))
    gok_list = [int(i) for i in gok]
    while True:
        for a in gok_list:
            if a > 6 or a < 1:
                print("Alleen getallen tussen de 1 en 6, raad nogmaals")
                secret()
                break
        if len(gok_list) != 4:
            print("Raad slechts 4 getallen, raad nogmaals")
            secret()
            break
        gok_list = [int(i) for i in gok]
        tel = 0
        zwart = 0 # zwarte pins krijgen
        for x in gok_list: # Aantal goed geraden klopt niet
            for y in passw:
                if x == y:
                    tel = tel + 1
                    break
        if gok_list == passw:
            print("GOED GERADEN!")
            break
        elif gok_list != passw:
            print(tel, "getallen goed geraden")
            print(passw)
            secret()
            break
# Menu
keuze = input("Welkom bij Mastermind! Kies een gamemode. \n[a] Raad de geheime code \n[b] Wees de gamemaster \n")
if keuze.lower() == "a":
    secret()
if keuze.lower() == "b":
    computer()

# def possibilities():
#     poss_list = []
#     for i in range(1, 7):
#         poss_list.append(i)
#         for j in range(1, 7):
#             poss_list.append(j)
#             for k in range(1, 7):
#                 poss_list.append(k)
#                 for l in range(1, 7):
#                     poss_list.append(l)
#     print(poss_list)

# possibilities()

