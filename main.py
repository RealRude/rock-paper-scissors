# Rock Paper Scissors from 12 Beginner Python Projects - Coding Course https://www.youtube.com/watch?v=8ext9G7xspg

print("")
import random


def play_the_game():

    user_choice = str(input("Welcome to Rock Paper Scissors. Please write 'r' for rock, 'p' for paper and 's' for scissors to play: "))

    # while loop to check for correct type of input from the user
    while user_choice != "r" and user_choice != "p" and user_choice != "s":

        user_choice = str(input("Only type 'r' or 'p' or 's' to make a choice. Please write 'r' for rock, 'p' for paper and 's' for scissors to play: "))
        continue

    # displaying the user choice in readable manner
    if (user_choice == 'r'):
        print("Your choice is rock.")
    elif (user_choice == 'p'):
        print("Your choice is paper.")
    else:
        print("Your choice is scissors.")

    # computer chooses
    three_choices = ('rock', 'paper', 'scissors')
    computer_plays = (random.choice(three_choices))
    print("Computer choise is " + computer_plays + ".")

    # extracts the first letter of the computer choice for easy one letter comparison with the user
    explode_choice = list(computer_plays)
    first_letter = explode_choice[0]
    computer_plays = first_letter

    #comparing choices of user and a computer and printing out the game results
    if (user_choice == computer_plays):
        print("It's a draw!")
    elif (user_choice == "r"):
        if (computer_plays == "p"):
            print("You've lost.")
        else:
            print("Congratulations, you've won!")
    elif (user_choice == "p"):
        if (computer_plays == "s"):
            print("You've lost.")
        else:
            print("Congratulations, you've won!")
    elif (user_choice == "s"):
        if (computer_plays == "r"):
            print("You've lost.")
        else:
            print("Congratulations, you've won!")


# calling the function for playing the game
play_the_game()

endprint = "\n\n>>>|END OF PROGRAM|<<<"
print(endprint)