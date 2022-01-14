import random

def start(lowest, highest):
    random_number = random.randint(lowest, highest)
    number = int(input(f"Guess a number from {lowest} to {highest} : "))
    while random_number != number:
        number = int(input(f"Guess a number from {lowest} to {highest} : "))
        if number > random_number:
            print("Too high")
        elif number < random_number:
            print("Too low")
        elif number == random_number:
            print(f"Congratulations, You have won the number was {random_number}")