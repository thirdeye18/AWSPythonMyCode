#!/usr/bin/python3
import requests
from dotenv import load_dotenv  # to handle .env file
import os  # to access the filesystem for the .env files

## Define NEOW URL
NEOURL = "https://api.nasa.gov/neo/rest/v1/feed?"

# this function grabs our credentials
# it is easily recycled from our previous script
def returncreds():
    ## first I want to grab my credentials
    # with open("/home/student/nasa.creds", "r") as mycreds:
    #     nasacreds = mycreds.read()
    ## remove any newline characters from the api_key
    # nasacreds = "api_key=" + nasacreds.strip("\n")
    # shorten above using .env method
    load_dotenv()
    nasacreds = os.getenv('NASA_KEY')
    print(type(nasacreds))
    return nasacreds

# this is our main function
def main():
    # startDate = input("Please enter a start date > ")
    endDate = input("Please enter an end date > ")

    ## first grab credentials
    nasacreds = returncreds()

    ## update the date below, if you like
    startdate = "start_date=2019-11-11"

    ## the value below is not being used in this
    ## version of the script
    # enddate = "end_date=END_DATE"

    # make a request with the request library
    print(NEOURL + startdate + "&" + nasacreds)
    neowrequest = requests.get(NEOURL + startdate + "&api_key=" + nasacreds)

    # strip off json attachment from our response
    neodata = neowrequest.json()

    ## display NASAs NEOW data
    print(neodata)

if __name__ == "__main__":
    main()

