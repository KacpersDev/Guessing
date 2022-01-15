from computer import computer_response

import random
import time

def start(lowest, highest, computer_reaction_time):  # correct number will be between lowest <> highest
    random_number = random.randint(lowest, highest)
    number = int(input(f"Guess a number from {lowest} to {highest} : "))
    computer(computer_reaction_time, lowest, highest, random_number)
    while random_number != number:
        number = int(input(f"Guess a number from {lowest} to {highest} : "))  # getting player input
        if number > random_number:
            print("Too high")  # Message will show if entered number by user is too high
            computer(computer_reaction_time, lowest, highest, random_number)
        elif number < random_number:
            print("Too low")  # Message will show if entered number by user is too low
            computer(computer_reaction_time, lowest, highest, random_number)
        elif number == random_number:
            return player_winner()  # Message will show if user guessed the number

def computer(computer_reaction_time, lowest, highest, correct_number):
    print("Waiting for computer to reply")
    time.sleep(computer_reaction_time)
    computer_response(lowest, highest, correct_number)  # computer is printing random number from lowest -> highest

def player_winner():
    return print("Player is the winner")
