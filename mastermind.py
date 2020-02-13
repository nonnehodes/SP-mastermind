import random
def secret_input():
    password = []
    while len(password) < 4:
        secret = int(input("Geef een getal tussen de 0 en 6: "))
        if secret > 6:
            print(" nder de 7 graag.")
        elif secret <= 6:
            password.append(secret)
    print(password)
# Menu
keuze = input("Welkom bij Mastermind! Kies een gamemode. \n[a] Gokken \n[b] Gamemaster \n")
if keuze.lower() == "a":
    print("Begin met gokken")
if keuze.lower() == "b":
    secret_input()


# def secret():
#     passw = []
#     while len(passw) < 4:
#         passw.append(random.randint(0, 6))
#     print(passw)
# secret()

# def possibilities():
#     poss_list = []
# possibilities()