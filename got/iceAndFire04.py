#!/usr/bin/python3
"""Alta3 Research - Exploring OpenAPIs with requests"""
# documentation for this API is at
# https://anapioficeandfire.com/Documentation

import requests
import pprint

AOIF_CHAR = "https://www.anapioficeandfire.com/api/characters/"
AOIF_HOUSE = "https://www.anapioficeandfire.com/api/houses/"

def main():
    ## user input for characters to search
    got_charToLookup = input("Pick a number between 1 and 1000 to return info on a GoT character! " )

    ## Send HTTPS GET to the API of ICE and Fire
    gotresp = requests.get(AOIF_CHAR + got_charToLookup)

    ## Decode the response
    got_dj = gotresp.json()
    # pprint.pprint(got_dj)

    # retrieve allegiance data
    houses = got_dj['allegiances']
    # get book list
    books = got_dj['books']

    ## returning house affiliation and books they appear in
    print(f"{got_dj['name']} AKA {got_dj['aliases']}")
    print("Owes Allegiance to:")
    for house in houses:
        houseresp = requests.get(house)
        decodedhouse = houseresp.json()
        print(decodedhouse['name'])
    print("Appears in:")
    for book in books:
        bookresp = requests.get(book)
        decodedbook = bookresp.json()
        print(decodedbook['name'])

if __name__ == "__main__":
    main()

