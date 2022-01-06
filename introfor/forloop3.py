#!/usr/bin/env python3
"""RZFeeser | Alta3 Research
   learning about for logic"""

# create list of dictionaries for farms
farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]

for farm in farms:
    print("\n" + farm.get("name"), end = ":\n")
    for agri in farm.get("agriculture"):
        print(agri, end = ", ")
    print("END OF FARM")
