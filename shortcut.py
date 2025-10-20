#!usr/bin/python3

#Joshua Krogstad
#10/24/2025

import subprocess

userInput = ""

while (True):
    #List all options
    print("[1] Create a symbolic link")
    print("[2] Delete a symbolic link")
    print("[3] Generate a symbolic link report")
    print("[4] Quit")

    #prompt user input
    userInput = input("Select an option: ")

    #if 1, run createSymLink

    #if 2, run deleteSymLink

    #if 3, run symLinkReport

    #if 4 or quit, quit
    if (userInput=="4" or userInput.lower()=="quit"):
        quit()
