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
    the string has to contain just letters and spaces
"""
def panagram_check(testString):
    # getting a list of only unique characters
    uniqueCharacters = find_uniques(string_to_lower_list(testString))
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
def prime_checker(num):
    if num < 2 or type(num) != int:
        print("Input must be a natural number >1 to check for prime")
        return False
    # loop from 2 to num checking if it is divisible by other numbers
    for i in range(2, num):
        if num % i == 0:
            print(f"{num} is not a prime number")
            return False
    print(f"{num} is a prime number")
    return True

""" splits a string into individual characters, remove white spaces, convert to lower
"""
def string_to_lower_list(inputString):
    returnList = list(inputString.lower().replace(" ", ""))
    return returnList

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

    # testing prime_checker
    prime_checker(1)
    prime_checker(2)
    prime_checker(29)
    prime_checker(3.14)


# this condition is only true if our script is run directly
# it is NOT true if our code is imported into another script
if __name__ == "__main__":
    main()
