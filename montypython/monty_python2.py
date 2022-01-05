#!/usr/bin/env python3

def main():
    # initialize round counter to 0
    round = 0
    # set up loop
    while True:
        #  increment round
        round = round + 1

        print('Finish the movie title, "Monty Python\'s The Life of ______"')
        answer = input("Your guess--> ")
        # correct answer given
        if answer == 'Brian':
            print('Correct')
            break
        # reached end of game with no correct answer
        elif round==3:
            print("Sorry, the answer was Brian.")
            break
        # loop back to beginning of while loop
        else:
            print("Sorry! Try again!")

main()
