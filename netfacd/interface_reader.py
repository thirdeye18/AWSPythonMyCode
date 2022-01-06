#!/usr/bin/env python3

# import statements
import netifaces

def print_IP(adapter):
    print("\nIP: ", end="")
    print(netifaces.ifaddresses(adapter)[netifaces.AF_INET][0]['addr'])

print(netifaces.interfaces())

# iterate over network interfaces
for i in netifaces.interfaces():
    print('\n**************Details of Interface - ' + i + ' *********************')
    try:
        print("MAC: ", end="")
        print(netifaces.ifaddresses(i)[netifaces.AF_LINK][0]['addr']) 
        print("IP: ", end="")
        print(netifaces.ifaddresses(i)[netifaces.AF_INET][0]['addr'])

    except: # for error message
        print("Could not find adapter information")

print_IP("lo")

