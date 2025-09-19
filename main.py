# auteur: Zhuo.H
# class: 407
# ce programme est un jeu de devinette de nombre


import random

def generator(smallest, biggest):
    g_answer = random.randint(smallest, biggest)
    return g_answer

first = int(input("choisi le plus petit nombre: "))
last = int(input("choisi le plus grand nombre: "))

number = generator(first, last)
tries = 0

limit = 10

print(f"J'ai choisi un nombre entre {first} et {last}. Essayer de trouver le nombre dans 10 essai.")

while True:
    if tries >= limit:
        print("vous n'avez plus d'essai...")
        io = input("voulez-vous recommencer? (appuyer'y'pour recommencer et 'n' pour quitter):  ")
        io == io.lower()
        if io == 'y':
            tries = 0
            first = int(input("choisi le plus petit nombre"))
            last = int(input("choisi le plus grand nombre"))
            number = generator(first, last)
            print(f"J'ai choisi un nombre entre {first} et {last}. Essayer de trouver le nombre dans 10 essai.")
            continue
        elif io == 'n':
            print("Merci! Au revoir!")
            break
        else:
            print("Écrivez 'y' ou 'n' la prochaine fois >:(")
            break
    answer = input("Écrivez votre premier réponse: ")

    if not answer.isdigit():
        print("votre réponse n'est pas une chiffre entier")
        continue
    answer = int(answer)
    if answer == number:
        print(f"Bravo! vous avez réussis en {tries + 1} essai!")
        io = input("voulez-vous recommencer? (appuyer'y'pour recommencer et 'n' pour quitter):  ")
        io == io.lower()
        if io == 'y':
            tries = 0
            first = int(input("choisi le plus petit nombre"))
            last = int(input("choisi le plus grand nombre"))
            number = generator(first, last)
            print(f"J'ai choisi un nombre entre {first} et {last}. Essayer de trouver le nombre dans 10 essai.")
            continue
        elif io == 'n':
            print("Merci! Au revoir!")
            break
        else:
            print("Écrivez 'y' ou 'n' la prochaine fois >:(")
            break

    elif answer < number:
        print(f"{answer} est plus petit que la réponse!")
    else:
        print(f"{answer} est plus grand que la réponse!")
    tries += 1
    print(f"vous avez: {limit - tries} essai restante")
