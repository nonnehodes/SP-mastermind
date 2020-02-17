import time
import random
from Feedback import feedback

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
    print("Uw geheime code is", secret_list)
    time.sleep(1)
    print("De computer gaat nu beginnen met raden.")
    mogelijkheden = [[i, j, k, l] for i in range(1, 7) for j in range(1, 7) for k in range(1, 7) for l in range(1, 7)]
    clean_list = mogelijkheden[:]
    pogingen = 0
    for i in mogelijkheden:
        pogingen = pogingen + 1
        eerste_gok = random.choice(mogelijkheden)
        eerste_feedback = feedback(eerste_gok, secret_list)
        verg_feedback = feedback(i, eerste_gok)
        if verg_feedback != eerste_feedback:
            clean_list.remove(i)
            print(eerste_gok)
        else:
            time.sleep(1)
            print("Geraden in", pogingen, "poging(en).")
            time.sleep(1)
            break
    if pogingen > 10:
        print("U heeft gewonnen!")
    if pogingen < 11:
        print("De computer heeft gewonnen :[")
    print(mogelijkheden)

def heuristiek(xxx):
    set_xxx = set(xxx)
    length = len(set_xxx)
    xxx.append(length)
    return xxx

def make_list():
    list = []
    for i in range(1, 7):
        for j in range(1, 7):
            for k in range(1, 7):
                for l in range(1, 7):
                    this_code = [i, j, k, l]
                    updated_code = heuristiek(this_code)
                    list.append(updated_code)
    sorted_list = []
    for j in range(4, 0, -1):
        for x in list:
            if x[4] == j:
                sorted_list.append(x[0:4])
    print(sorted_list)
    return sorted_list
make_list()

