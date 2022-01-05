#!/usr/bin/env python3

def main():
    # initialize round counter to 0 and answer to blank
    round = 0
    answer = " "

    # set up loop
    while round < 3 and (answer.lower() != "brian" and answer.lower() != "shrubbery"):
        #  increment round
        round += 1 

        answer = input("Finish the movie title, \"Monty Python\'s The Life of ______: ")
        # correct answer given
        if answer.lower() == 'brian':
            print('Correct')
        elif answer.lower() == "shrubbery":
            print("You gave the super secret answer")
        # reached end of game with no correct answer
        elif round==3:
            print("Sorry, the answer was Brian.")
        # loop back to beginning of while loop
        else:
            print("Sorry! Try again!")

main()
