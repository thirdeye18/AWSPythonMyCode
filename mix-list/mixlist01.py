#!/usr/bin/env python3
# create a list containing three items
my_list = ["192.168.0.5", 5060, "UP"]
# display first item
print("The first item in the list (IP): " + my_list[0] )
# Below needs to be cast from an int to a str for printing
print("The second item in the list (port): " + str(my_list[1]) )
# displaying the final item
print("The third item in the list (state): " + my_list[2] )

iplist = [ 5060, "80", 55, "10.0.0.1", "10.20.30.1", "ssh" ]

print(iplist[3:5])
