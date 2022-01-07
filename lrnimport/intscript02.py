#!/usr/bin/env python3
# This script will fail!!!
# because the script is the same name as the module being imported from
# it tries to import call() from this script, not the module

import subprocess

subprocess.call(["ip", "link", "show", "up"])
print("This program will check your interfaces.")
interface = input("Enter an interface, like, ens3: ")
subprocess.call(["ip", "addr", "show", "dev", interface])
subprocess.call(["ip", "route", "show", "dev", interface])

