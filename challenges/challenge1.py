#!/usr/bin/env python3

""" takes a list and returns a new list with unique elements of the first list
"""
def find_uniques(items):
    uniques = []
    for item in items:
        if item not in uniques:
            uniques.append(item)
    return uniques

""" check whether a string is a pangram or not, does not work if punctuation
    or digits are present
    teh string has to contain just letters and spaces
"""
def panagram_check(testString):
    # split string to individual characters, remove white space and convert to lower case
    testList = list(testString.lower().replace(" ", ""))
    # getting a list of only unique characters
    uniqueCharacters = find_uniques(testList)
    if len(uniqueCharacters) == 26:
        print("The provided string is a panagram")
        return True
    # string is not panagram
    print("The provided string is not a panagram")
    return False

""" accepts a hyphen-separated sequence of words as input and prints the words 
    in a hyphen-separated sequence after sorting them alphabetically
"""
def hyphen_sorted():

    return null

""" takes a number as a parameter and check the number is prime or not
"""
def prime_checker():
    
    return null

""" Run-time code"""
def main():
    # testing find_uniques
    samplelist1 = [1,2,3,3,3,3,4,5]
    print(find_uniques(samplelist1))

    # testing panagram_check
    sampleString1 = "The quick brown fox jumps over the lazy dog"
    sampleString2 = "This is a test string"
    panagram_check(sampleString1)
    panagram_check(sampleString2)

# this condition is only true if our script is run directly
# it is NOT true if our code is imported into another script
if __name__ == "__main__":
    main()
