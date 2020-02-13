# Imports
import random
import time

# De computer raadt
# def secret_input():
#     password = []
#     while len(password) < 4:
#         secret = int(input("Geef een getal tussen de 0 en 6: "))
#         if secret > 6:
#             print("Onder de 7 graag.")
#         elif secret <= 6:
#             password.append(secret)
#     print("Jouw geheime code is", password)
#     time.sleep(2)
#     print("De computer gaat nu beginnen met raden")
# secret_input()

def computer():
    password = []
    secret = input("Maak een geheime code aan met 4 getallen tussen de 0 en 6: ")
    secret_list = [int(i) for i in secret]
    for x in secret_list:
        if x > 6:
            secret = input("Maak een geheime code aan met 4 getallen tussen de 0 en 6: ")
            print("Gebruik alleen getallen onder de 7.\n", secret)
    if len(secret_list) != 4:
        secret = input("Maak een geheime code aan met 4 getallen tussen de 0 en 6: ")
        print("Maak een 4 cijferige code aan.\n", secret)
    print(secret_list)
computer()



# De speler raadt
# passw = []
# while len(passw) < 4:
#     passw.append(random.randint(0, 6))
# def secret():
#
#     gok = str(input("Raad 4 getallen tussen de 0 en 6: "))
#     gok_list = [int(i) for i in gok]
#     while True:
#         for a in gok_list:
#             if a > 6:
#                 print("Alleen getallen tussen de 0 en 6, raad nogmaals")
#                 continue
#         if len(gok_list) != 4:
#             print("Raad slechts 4 getallen, raad nogmaals")
#             continue
#         gok_list = [int(i) for i in gok]
#         tel = 0
#         zwart = 0 # zwarte pins krijgen
#         for x in gok_list: # Aantal goed geraden klopt niet
#             for y in passw:
#                 if x == y:
#                     tel = tel + 1
#                     break
#         if gok_list == passw:
#             print("GOED GERADEN!")
#             break
#         elif gok_list != passw:
#             print(tel, "getallen goed geraden")
#             print(passw)
#             secret() # ik wil dat de geheime code hetzelfde blijft en niet opnieuw wordt aangemaakt
#             break

# # Menu
# keuze = input("Welkom bij Mastermind! Kies een gamemode. \n[a] Raad de geheime code \n[b] Wees de gamemaster \n")
# if keuze.lower() == "a":
#     secret()
# if keuze.lower() == "b":
#     secret_input()

# def possibilities():
#     poss_list = []
# possibilities()