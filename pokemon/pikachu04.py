#!/usr/bin/python3

import requests
## for working with data in lots of formats
## python3 -m pip install pandas
import pandas

# define base URL
POKEURL = "http://pokeapi.co/api/v2/pokemon/"

def main():

    # Make HTTP GET request using requests, and decode
    # JSON attachment as pythonic data structure
    # Augment the base URL with a limit parameter to 1000 results
    pokemon = requests.get(f"{POKEURL}?limit=1000")
    pokemon = pokemon.json()

    # Loop through data, move names to list
    names = []
    for poke in pokemon["results"]:
        names.append(poke.get("name"))   

    print(f"Total number of Pokemon returned: {len(pokemon['results'])}")

    ## export to excel with pandas
    # make a dataframe from our data
    pokedf = pandas.DataFrame(names)
    # export to MS Excel XLSX format
    # run the following to export to XLSX
    # index=False prevents the index from our dataframe from
    # being written into the data
    pokedf.to_excel("pokemons.xlsx", index=False)

    # export to json
    pokedf.to_json(r'pokemons.json')

if __name__ == "__main__":
    main()

