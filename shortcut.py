#!usr/bin/python3

#Joshua Krogstad
#10/24/2025

import subprocess
import os

#Search for file given filename
def findFile(fileName):
    paths = []
    #Ignores directories user does not have access to
    #Recursively search every directory
    for dirPath, dirNames, fileNames in os.walk('/'):
        for name in fileNames:
            #If a matching filename is found
            if (name==fileName):
                #Add full path of file to paths
                paths.append(dirPath + "/" + name)
    return paths

#Select one from a list of multiple items
def selectFromMultiple(optionList):
    print("Multiple files with the provided name were found:")
    #Print all options
    for i in range(len(optionList)):
        print("[" + str(i+1) + "] " + optionList[i])
    choice = -1
    choice = input("Please select the file you want to create a shortcut for: ")
    #If choice is within given range
    if (int(choice) > 0 & int(choice) <= len(optionList)):
        #Return the value of selected choice
        return optionList[int(choice)-1]
    #If choice is invalid, loop through again
    print("\tInvalid choice, please try again")
    return selectFromMultiple(optionList)

#Create symbolic link to selected file on desktop
def createSymLink():
    file = input("Enter filepath to make symbolic link to: ")
    #Find all valid filepaths with same filename
    fullPaths = findFile(file)
    #No matches
    if (len(fullPaths) == 0):
        print("\tFile not found, please check the file name and try again")
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

#Return a list of all symbolic links on the user desktop
def findAllLinks():
    allFiles = os.listdir("~/Desktop/")
    print(allFiles)

#Delete a symbolic link
def deleteSymLink():
    #Find all symbolic links
    allLinks = findAllLinks()
    #Allow user to select which link to delete (add a "Back" option in list)
    #Delete that link

#Create a file
def symLinkReport():
    print("NOT IMPLEMENTED")


userInput = ""

while (True):
    
    #clear terminal each loop
    #os.system("clear")

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
