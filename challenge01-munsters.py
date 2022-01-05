#!/usr/bin/env python3

"""Alta3 Research | RZFeeser
   Review of Lists and Dictionaries"""

# define a short data set (in real world, we want to read this from a file or API)
munsters = {'endDate': 1966, 'startDate': 1964,\
        'names':['Lily', 'Herman', 'Grandpa', 'Eddie', 'Marilyn']}   # {} creates dict

# Your solution goes below this line
# ----------------------------------

print("Values associated with \"names\":")
print(munsters.get("names"))

print("Values associated with \"enddate\":")
print(munsters.get("endDate"))


print("Values associated with \"startDate\":")
print(munsters.get("startDate"))

print("Adding new key \"episodes\".")
munsters["episodes"] = 70
print(munsters)
