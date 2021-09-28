
wizard = "Wizard"
elf = "Elf"
human = "Human"
orc = "Orc"
wizard_hp = 70
elf_hp = 100
human_hp = 150
orc_hp = 170

wizard_damage = 150
elf_damage = 100
human_damage = 20
orc_damage = 200

dragon_hp = 300
dragon_damage = 50


while True:
    character = input(
        " 1) Wizard \n 2) Elf \n 3) Human \n Choose Your Character:")
    character = character.lower()

    if character == "1" or character == "wizard":

        character = wizard

        my_hp = wizard_hp
        my_damage = wizard_damage

        break
    if character == "2" or character == "elf":

        character = elf
        my_hp = elf_hp
        my_damage = elf_damage

        break
    if character == "3" or character == "human":
        character = human
        my_hp = human_hp
        my_damage = human_damage

        break
    if character == "4" or character == "orc":
        character = orc
        my_hp = orc_hp
        my_damage = orc_damage

        break
    if character == "5" or character == "exit":
        break

    else:
        print("Unknown Character, please enter a valid selection")

        print("You have chosen the character: " + character)
        print("Health: " + str(my_hp))
        print("damage: " + str(my_damage) + "\n")

while True:
    dragon_hp = int(dragon_hp) - int(my_damage)

    if my_hp >= 0:
        print("The " + character + " damaged the Dragon!")
        print("The Dragon's hitpoints are now: " + str(dragon_hp) + "\n")

    if dragon_hp <= 0:

        print("The Dragon has lost the battle")

        break

    if dragon_hp >= 0:
        my_hp = int(my_hp) - int(dragon_damage)
        print("The Dragon strikes back at " + character)
        print("The " + character +
              "'s hitpoints are now : " + str(my_hp) + "\n")

    if my_hp <= 0:

        print("The " + character + " has lost the battle")
        break

        # message = input("1)Yes, 2)No \n Please enter your choice")

        # print("")

        # if message == "Yes":
        #     print("ok")
