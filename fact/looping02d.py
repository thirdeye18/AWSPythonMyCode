#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   For - Looping across a file opened with 'with'
         while also being gentle on memory consumption.
         Sort domains ending in .org and .com into files
         org-domain.txt and com-domain.txt."""

# open file in read mode
with open("dnsservers.txt", "r") as dnsfile:
    #indent keeps dnsfile open
    # loop over lines directly from the file without creating variable
    for svr in dnsfile:
        svr = svr.rstrip('\n')  #remove newline if there is one
        # check the ending of the string to sort it
        if svr.endswith('org'):
            with open("org-domain.txt", "a") as srvfile:
                srvfile.write(svr + "\n")
        elif svr.endswith('com'):
            with open("com-domain.txt", "a") as srvfile:
                srvfile.write(svr + "\n")
    
# no need to close the file - done automatically

