#!/usr/bin/env python3
"""Justin Hammel - thirdeye18
   Simple rock paper scissors with conditionals
   if, elif, else - A simple program using conditionals to make a decision."""

#import statements
import random

cpu = random.randrange(1,4)

# rock = 1, paper = 2, scissors = 3
prompt = 'Please choose (R)ock, (P)aper, or (S)cissors. '
rock = "rock beats scissors"
paper = "paper beats rock"
scissors = "scissors beats paper"
tie = "There was a tie"

# accept user input
choice = input(prompt)

# evaluating users input
if choice.lower() == "r":
    if cpu == 1:
        message = tie
    elif cpu == 2:
        message = paper
    else:
        message = rock

elif choice.lower() == "p":
    if cpu == 1:
        message = paper 
    elif cpu == 2:
        message = tie
    else:
        message = rock

elif choice.lower() == "s":
    if cpu == 1:
        message = rock
    elif cpu == 2:
        message = paper
    else:
        message = tie
else:
    message = "Please make a valid choice"

if cpu == 1:
    print("CPU chooses ROCK")
elif cpu == 2:
    print("CPU chooses PAPER")
else:
    print("CPU chooses SCISSORS")

print(message)

