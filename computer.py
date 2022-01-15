
import random

def computer_response(lowest, highest, correct_number):  # printing computer response
    random_number = random.randint(lowest, highest)
    while random_number != correct_number:
        return print(f"Computer entered: {random_number}")
    if random_number == correct_number:
        return computer_winner()

def computer_winner():
    return print("Computer is the winner")
