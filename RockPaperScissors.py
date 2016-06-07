# Author:   Matty T.
# Date:     4 June 2016
# Abstract: A simple "Rock, Paper, Scissors" game.

import random
import time
import sys

# Variables to track the game score.
user_score = 0
computer_score = 0
# An initial welcome message that runs once when the program runs.
print("Let's play Rock, Paper, Scissors!\n")


# Get user's throw as input. Convert to all lower case for string comparison.
def get_user_throw():
    user_throw = input("Choose rock, paper, or scissors: ")
    user_throw = user_throw.lower()
    # Take user's throw and convert it to an integer: 1, 2, or 3.
    if user_throw == "rock":
        user_throw = 1
        successful_throw = True
    elif user_throw == "paper":
        user_throw = 2
        successful_throw = True
    elif user_throw == "scissors":
        user_throw = 3
        successful_throw = True
    # Error handling in case of spelling errors or intentional subterfuge.
    else:
        successful_throw = False
    # Return the user's throw as an integer, or as a zero in the case of an error.
    if successful_throw:
        return user_throw
    else:
        return 0


# Generate a random integer between 1 and 3 representing the computer's throw. Returns an integer.
def get_computer_throw():
    computer_throw = random.randint(1, 3)
    return computer_throw


# Compare the user's throw with the randomly generated computer throw. Returns an integer.
def compare_throws(user, computer):
    if user == computer:
        result = 0
    # Rock = 1, paper = 2, and scissors = 3. The throws are therefore compared mathematically.
    elif user == int(computer) + 1 or user == int(computer) - 2:
        result = 1
    else:
        result = 2
    return result

# Loops the game process while playing. Sets 'playing' to false on quit and exits the program.
playing = True
while playing:
    # Handles any errors in the user's input and loops again in the event of an error.
    user_error = True
    while user_error:
        # Calls the function to take in user input. Loops again for unexpected input.
        my_throw = get_user_throw()
        if my_throw != 0:
            user_error = False
        else:
            print("\nTry again! Choose rock, paper, or scissors. Maybe check your spelling.\n")
            continue

    print("\nRock, paper, scissors, shoot!\n")
    # Builds suspense.
    time.sleep(1)

    # Prints the user's throw.
    if my_throw == 1:
        print("You chose ROCK!")
    elif my_throw == 2:
        print("You chose PAPER!")
    elif my_throw == 3:
        print("You chose SCISSORS!")
    # Superfluous error handling.
    else:
        print("You made an ERROR!")

    # Calls the function to get the computer's throw, then prints it.
    their_throw = get_computer_throw()
    if their_throw == 1:
        print("The computer chose ROCK!")
    elif their_throw == 2:
        print("The computer chose PAPER!")
    elif their_throw == 3:
        print("The computer chose SCISSORS!")
    # Superfluous error handling.
    else:
        print("The computer made an ERROR!")

    # Calls the functions to compare the two throws and determine a winner.
    winner = compare_throws(my_throw, their_throw)

    # Prints the winner of the round.
    if winner == 0:
        print("It's a draw!\n")
    elif winner == 1:
        print("You win this round!\n")
        user_score += 1
    else:
        print("The computer wins this round!\n")
        computer_score += 1

    # Gives the user the option to play again or not.
    again = input("Play again? ")
    again = again.lower()
    # If the user chooses to play again, prints the current score and loops through the whole process.
    if again == "yes" or again == "y" or again == "":
        print("\nYour score: " + str(user_score))
        print("Computer score: " + str(computer_score) + "\n")
        continue
    # If the user chooses not to play again, sets playing to False to exit the while loop.
    else:
        playing = False

# A final scoreboard and thank you message.
print("\nFINAL SCORE\nYou: " + str(user_score) + "\nCPU: " + str(computer_score))
print("\nThanks for playing!")

sys.exit()
