#!/usr/bin/env python3

"""A simple script to move two files into ceph_storage/
   Alta3 Research | rzfeeser@alta3.com"""

# import statements
import shutil
import os


def main():
    """called at run-time"""
    # change current working directory
    os.chdir("/home/student/AWSPythonMyCode/")

    # move file to specified path if file already exists it will be overwritten
    shutil.move("raynor.obj", "ceph_storage/")

    # prompt for new name for a file prior to moving
    xname = input("What is the new name for kerrigan.obj? ")
    # moving file with the new name
    shutil.move("ceph_storage/kerrigan.obj", "ceph_storage/" + xname)


