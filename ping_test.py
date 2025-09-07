#!/usr/bin/python3
#Shebang
import os

#Joshua Krogstad, 9/5


#Clear terminal
os.system("clear")

#Displays default gateway
def display_default_gateway():
    os.system("ip r | awk '{print $3}'")

#
def local_connectivity():
    print("UNIMPLEMENTED")

#
def remote_connectivity():
    print("UNIMPLEMENTED")

#
def DNS_resolution():
    print("UNIMPLEMENTED")

option = 0
while(option != 5):
    #Display options
    print("1. Display the default gateway")
    print("2. Test Local Connectivity")
    print("3. Test Remote Connectivity")
    print("4. Test DNS Resolution")
    print("5. Exit/quit the script")
    
    #Get user input
    option = int(input("Select an option: "))
    #print(option) #DEBUG

    if(option == 1):
        display_default_gateway()
    
    elif(option == 2):
        local_connectivity()
    
    elif(option == 3):
        remote_connectivity()
        
    elif(option == 4):
        DNS_resolution()
