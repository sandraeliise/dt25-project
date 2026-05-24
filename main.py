import random

print("==== KOOLIST PÕGENEMINE ====")

name = input("Sisesta oma nimi: ")
#mängija HP
hp = 20
key = False
#mängu algus
print("\nSa ärkad öises koolis.")
print("Kõik on pime ja vaikne.")

while True:

    print("\nMida soovid teha?")
    print("1 - Ava kapp")
    print("2 - Ava uks")
    print("3 - Vaata HP-d")

    valik = input("> ")

    if valik == "1":
#kas mängija leidis võtme
        if key == False:
            print("\nLeidsid võtme!")
            key = True
        else:
            print("\nKapp on tühi.")

    elif valik == "2":
#kontrollib kas mängijal on võti
        if key == True:
            print("\nSa avasid ukse.")
            break
        else:
            print("\nUks on lukus.")

    elif valik == "3":
        print("\nSinu HP on", hp)

    else:
        print("\nVale valik.")

print("\nSa jõudsid koridori.")

print("Kuskilt tuleb koristaja!")
#enemy HP
enemy_hp = 15 
print("Mäng käivitub")

while enemy_hp > 0 and hp > 0:

    print("\nSinu HP:", hp)
    print("Koristaja HP:", enemy_hp)

    print("\n1 - Ründa")
    print("2 - Põgene")
#battle süsteem
    attack = input("> ")

    if attack == "1":

        dmg = random.randint(3, 6)
        enemy_hp -= dmg

        print("\nTegid", dmg, "damage!")

        if enemy_hp > 0:

            enemy_dmg = random.randint(2, 5)
            hp -= enemy_dmg

            print("Koristaja lõi sind", enemy_dmg, "damagega!")

    elif attack == "2":

        print("\nSa ei saanud põgeneda.")

        enemy_dmg = random.randint(2, 5)
        hp -= enemy_dmg

        print("Koristaja lõi sind", enemy_dmg, "damagega!")

    else:
        print("\nVale valik.")

if hp > 0:
    print("\nSa põgenesid koolist!")
    print("Võitsid mängu!")

else:
    print("\nGame over.")