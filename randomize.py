import random
pips = random.randint(1, 6)
print(pips)

prizes = ["a car", "$1000", "a pony"]
prize_won = random.choice(prizes)
print(prize_won)
cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
random.shuffle(cards)
print(cards)
