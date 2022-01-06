#!/usr/bin/python3

# parse keystone.common.wsgi and return number of failed login attempts
loginfail = 0 # counter for fails
loginsuccess = 0    # counter for successful logins

# open the file for reading
with open("/home/student/AWSPythonMyCode/attemptlogin/keystone.common.wsgi") as kfile:

    # loop over the file
    for line in kfile:
        # if this 'fail pattern' appears in the line...
        if "- - - - -] Authorization failed" in line:
            loginfail += 1 # this is the same as loginfail = loginfail + 1
            print("Failed login from " + line.split(" ")[-1])
        elif "-] Authorization failed" in line:
            loginsuccess += 1

print("The number of failed log in attempts is", loginfail)
print(f"The number of successfull login attempts is {loginsuccess}")

