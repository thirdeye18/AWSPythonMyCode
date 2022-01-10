#!/usr/bin/env python3
"""Alta3 Research
   Star Wars API HTTP response parsing"""

# pprint makes dictionaries a lot more human readable
from pprint import pprint

# requests is used to send HTTP requests (get it?)
import requests

# URL = "https://swapi.dev/luke/force"      # Comment out this line
URL= "https://swapi.dev/api/people/4/"     # Uncomment this line
# URL_film = "https://swapi.dev/api/films/1/"
# URL_ship = "https://swapi.dev/api/starships/13/"

def main():
    """sending GET request, checking response"""

    # SWAPI response is stored in "resp" object
    resp= requests.get(URL)

    # check to see if the status is anything other than what we want, a 200 OK
    if resp.status_code == 200:
        # convert the JSON content of the response into a python dictionary
        vader= resp.json()
        # pprint(vader)

        print(f"{vader['name']} was born in the year {vader['birth_year']}. His eyes are {vader['eye_color']} and his hair color is {vader['hair_color']}. ")

    else:
        print("That is not a valid URL.")

    film = requests.get("https://swapi.dev/api/films/1/").json()
    ship = requests.get("https://swapi.dev/api/starships/13/").json()
    print(f"He first appeared in {film['title']} and could be flying around in his {ship['name']}.")

if __name__ == "__main__":
    main()

