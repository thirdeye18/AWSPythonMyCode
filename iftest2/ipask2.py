#!/usr/bin/env python3

"""Alta3 Research | RZFeeser
    Conditionals - strings test true"""

ipchk = input("Apply an IP address: ")

# a string tests as true
if ipchk == "192.168.70.1":
    print(f"Looks like the gateway address was set: {ipchk}")
elif ipchk:
    print(f"Looks like the IP address was set: {ipchk}")
else:   #data not provided
    print("You did not enter an IP address")
