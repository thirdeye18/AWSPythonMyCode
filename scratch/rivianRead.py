#!/usr/bin/env python3

""" Justin Hammel
    Script reads the rivian.txt file and displays the data to the screen
"""
def main():
    with open("rivian.txt", "r") as dataIn:
        for line in dataIn:
            print(line)

main()
