#!/usr/bin/env python3
# Alta3 Research || Author: RZFeeser@alta3.com
# Check hostname against expected value

# collect user input
hostname = input("What value should we set for the hostname? ")
# input scrubbing with lower method
if hostname.lower() == "mtg":
    print("The hostname was mtg")
    print("hostname matches expected config")

print("Exiting the script")
