#!/usr/bin/env python3

fileName = input("Please enter the name of a file to read: ")

## create file object in "r"ead mode
with open(fileName, "r") as configfile:
    ## readlines() creates a list by reading target
    ## file line by line
    # configlist = configfile.read().splitlines()

    configlist = [line.strip() for line in configfile]
    # line below does not work
    # print(f"{(line.strip() for line in configfile).len()} lines in file")

## file was just auto closed (no more indenting)

## each item of the list now has the "\n" characters back
print(configlist)

# Printing the number of lines fro the original file
print("vlanconfig.cfg contains ", len(configlist), "lines")




