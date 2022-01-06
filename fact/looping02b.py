#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   For - Using a file's lines as a source for the for-loop"""

# open file in read mode
with open("dnsservers.txt", "r") as dnsfile:
    #indent keeps dnsfile open
    # create list of lines
    dnslist = dnsfile.readlines()
    # loop over lines
    for svr in dnslist:
        #print and end without a newline
        print(svr, end="") # the line we read ALREADY contains a \n (newline)
    
# no need to close the file - done automatically

