#!usr/bin/python3

#Joshua Krogstad
#10/24/2025

import subprocess
import os

def findFile(fileName):
    files = os.system("sudo find / -name \"" + fileName+ "\"")
    print(files)

def createSymLink():
    filePath = input("Enter filepath to make symbolic link to: ")
    findFile(filePath)
    fileName = input("Enter name for symbolic link: ")
    os.system("ln -s " + filePath + " $HOME/Desktop/" + fileName)

def deleteSymLink():
    print("NOT IMPLEMENTED")

def symLinkReport():
    print("NOT IMPLEMENTED")


userInput = ""

while (True):
    
    #clear terminal each loop
    os.system("clear")

    #List all options
    print("[1] Create a symbolic link")
    print("[2] Delete a symbolic link")
    print("[3] Generate a symbolic link report")
    print("[4] Quit")

    #prompt user input
    userInput = input("Select an option: ")

    #if 1, run createSymLink
    if (userInput=="1"):
        createSymLink()

    #if 2, run deleteSymLink
    if (userInput=="2"):
        deleteSymLink()

    #if 3, run symLinkReport
    if (userInput=="3"):
        symLinkReport()

    #if 4 or quit, quit
    if (userInput=="4" or userInput.lower()=="quit"):
        print("\tQuitting...")
        quit()
