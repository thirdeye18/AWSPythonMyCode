#!/usr/bin/env python3

"""Alta3 Research | RZFeeser
    Conditionals - strings test true"""

ipchk = input("Apply an IP address: ")

# a string tests as true
if ipchk:
    print(f"Looks like the IP address was set: {ipchk}")
else:   #data not provided
    print("You did not enter an IP address")
