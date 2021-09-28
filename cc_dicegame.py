import random


high_score = 0


def dice_game():

    global high_score

    while True:
        print("\nCurrent High Score:", high_score)
        print("1) Roll Dice")
        print("2) Leave Game")
        option = input("\nEnter your choice:")

        if option == "1":
            roll_one = random.randint(1, 6)
            roll_two = random.randint(1, 6)
            total = roll_one + roll_two

            print("You roll a...", roll_one)
            print("You roll a...", roll_two)
            print("You have rolled a total of:", total)

            if total > roll_one and total > roll_two:

                high_score = total
                print("\nNew High Score!")

        if option == "2":

            print("\nGoodbye!\n")
            break


dice_game()
