import random

print("Welcome to Snack Water Gun Game!")
print("You have 3 chances to beat the computer.")

chances = 3
while chances > 0:
    player = input("Choose 'snack' or 'water gun': ").lower()
    computer = random.choice(["snack", "water gun"])

    if player == computer:
        print("Draw! Try again.")
    elif player == "snack":
        print("You lose! Computer wins with a water gun.")
    else:
        print("You win! Computer loses with a snack.")
        break

    chances -= 1

print("Game Over.")
