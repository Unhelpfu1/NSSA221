#!usr/bin/python3

#Joshua Krogstad
#10/24/2025

import subprocess
import os

#Search for file given filename
def findFile(fileName):
    files = subprocess.run(args=["sudo", "find", "/", "-name", "\""+fileName+"\""], stdout=subprocess.PIPE).stdout.decode('utf-8')
    print(files)
    #to return later
    paths = []
    #for each line found
    for line in files:
        #if line is not empty and starts with / filepath
        if (line!="" & line[0]=="/"):
            paths.append(line)
    return paths

#Select one from a list of multiple items
def selectFromMultiple(optionList):
    print("Multiple files with the provided name were found:")
    #Print all options
    for i in range(len(optionList)):
        print("[" + i+1 + "] " + optionList[i])
    choice = input("Please select the file you want to create a shortcut for: ")
    #If choice is within given range
    if (choice > 0 & choice <= len(optionList)):
        #Return the value of selected choice
        return optionList[choice-1]
    #If choice is invalid, loop through again
    print("\tInvalid choice")
    return selectFromMultiple(optionList)

#Create symbolic link to selected file on desktop
def createSymLink():
    file = input("Enter filepath to make symbolic link to: ")
    #Find all valid filepaths with same filename
    fullPaths = findFile(file)
    #No matches
    if (len(fullPaths) == 0):
        print("\tFile not found")
        return
    #One match
    if (len(fullPaths) == 1):
        filePath = fullPaths[0]
    #Multiple matches
    if (len(fullPaths) > 1):
        filePath = selectFromMultiple(fullPaths)
    fileName = input("Enter name for symbolic link: ")
    #Create the symbolic link
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
