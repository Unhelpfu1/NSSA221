#!/usr/bin/python3

#Joshua Krogstad
#10/24/2025

import os
from datetime import datetime

#Search for file given filename
def findFile(file_name):
    paths = []
    #Ignores directories user does not have access to
    #Recursively search every directory
    for dir_path, dir_names, file_names in os.walk('/'):
        for name in file_names:
            #If a matching filename is found
            if (name==file_name):
                #Add full path of file to paths
                paths.append(dir_path + "/" + name)
    return paths

#Select one from a list of multiple items
def selectFromMultiple(option_list):
    #Print all options
    for i in range(len(option_list)):
        print("[" + str(i+1) + "] " + option_list[i])
    choice = -1
    choice = input("Please select the file you would like to interact with: ")
    #If choice is within given range
    if (int(choice) > 0 and int(choice) <= len(option_list)):
        #Return the value of selected choice
        return option_list[int(choice)-1]
    #If choice is invalid, loop through again
    print("\tInvalid choice, please try again")
    return selectFromMultiple(option_list)

#Create symbolic link to selected file on desktop
def createSymLink():
    file = input("Enter filepath to make symbolic link to: ")
    #Find all valid filepaths with same filename
    full_paths = findFile(file)
    #No matches
    if (len(full_paths) == 0):
        print("\tFile not found, please check the file name and try again")
        return
    #One match
    if (len(full_paths) == 1):
        file_path = full_paths[0]
    #Multiple matches
    if (len(full_paths) > 1):
        file_path = selectFromMultiple(full_paths)
    file_name = input("Enter name for symbolic link: ")
    #Create the symbolic link
    os.system("ln -s " + file_path + " $HOME/Desktop/" + file_name)

#Return a list of all symbolic links on the user desktop
def findAllLinks():
    #Read user desktop directory
    all_items = os.scandir(os.path.expanduser("~/Desktop"))
    all_links = []
    #Sort symlinks from non symlinks
    for item in all_items:
        if (item.is_symlink()):
            all_links.append(item.path)
    return all_links

#Delete a symbolic link
def deleteSymLink():
    #Find all symbolic links
    all_links = findAllLinks()
    #Allow user to select which link to delete (add a "Back" option in list)
    all_links.append("Back")
    choice = selectFromMultiple(all_links)
    #Delete that link
    if (choice != "Back"):
        os.system("rm " + choice)
#os.readlink to find destination of symlink

#Create a file with all current links on desktop in it
def symLinkReport():
    #Get all links
    all_links = findAllLinks()
    #Create Report and add header
    date_string = datetime.today().strftime('%Y-%m-%d;%H:%M:%S')
    report = "Symbolic Link Report\t-\t" + date_string + "\n"
    #add link to list, then "-> <destination>"
    for link in all_links:
        report += link + " \t-> " + os.readlink(link) + "\n"
    #write total lines
    report += "Total links on desktop: " + str(len(all_links) + "\n")
    #save report to new file in home directory
    new_filename = "symLinkReport_" + date_string + ".log"
    with open(new_filename, 'w') as file:
        file.write(report)

user_input = ""

#clear terminal at start
os.system("clear")

while (True):
    
    #print cwd
    print("Current directory: " + os.getcwd())

    #List all options
    print("[1] Create a symbolic link")
    print("[2] Delete a symbolic link")
    print("[3] Generate a symbolic link report")
    print("[4] Quit")

    #prompt user input
    user_input = input("Select an option: ")

    #if 1, run createSymLink
    if (user_input=="1"):
        createSymLink()

    #if 2, run deleteSymLink
    if (user_input=="2"):
        deleteSymLink()

    #if 3, run symLinkReport
    if (user_input=="3"):
        symLinkReport()

    #if 4 or quit, quit
    if (user_input=="4" or user_input.lower()=="quit"):
        print("\tQuitting...")
        quit()

    #add newline for readability
    print()
