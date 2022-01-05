#!/usr/bin/env python3

# import statements
import shutil
import os

def main():
    # moving to working directory
    os.chdir("/home/student/AWSPythonMyCode")
    # copy single file
    shutil.copy("5g_research/sdn_network.txt", "5g_research/sdn_network.txt.copy")
    # copy entire directory will create directory if it does not exist
    # removing directory to prevent error if the new directory already exists
    os.system("rm -rf /home/student/AWSPythonMyCode/5g_research_backup/")
    shutil.copytree("5g_research/", "5g_research_backup/")

if __name__ == "__main__":
    main()
