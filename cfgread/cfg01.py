#!/usr/bin/env python3

######## EXPLORE READ ##########
## create file object in "read mode
configfile = open("vlanconfig.cfg", "r")

## display file to the screen - .read()
print(configfile.read())

## close file
configfile.close()


######## EXPLORE READLINES ##########
## re-create file object to explore new method
configfile = open("vlanconfig.cfg", "r")

## make a list of file lines - .readlines()
configlist = configfile.readlines()
print(configlist)

## Iterate through configlist
for x in configlist:
    print(x, end = "")
    print(x.rstrip())
    print(x.strip())

## Always close your file
configfile.close()

