# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 08:13:28 2023

@author: hnewey7
"""

import atexit
import os

# Initialisation function.
def init():
    
    # Get log file path.
    folderPath = os.path.dirname(os.path.abspath(__file__))
    logPath = folderPath + "\\logs.txt"
    
    # Check if file exists.
    if os.path.exists(logPath):
        
        # Read file.
        log = open(logPath,"r")
        data = log.readlines()     
        
        # Get statistics and stack from data.
        numberRead = data[0]
        stack = data[1:len(data)-1]

    else:
        # Create log path.
        log = open(logPath,"x")
        
        # Set numberRead to zero.
        numberRead = 0
        stack = []
        
    return logPath, numberRead, stack 

# Function to save data on close.
def onClose(logPath, numberRead, stack):
    
    log = open(logPath, 'w')
    
    # Writing data to log.
    log.write(str(numberRead))
    log.write(stack)
    
    # Saving log file.S
    log.close()
    
# Main function.
def main():
    
    if len(stack) == 0:  
        # Set stats if no stack.
        currentRead = "Not reading anything currently."
        numberBook = 0
    
    else:
        # Get stats when valid stack.
        currentRead = stack[0]
        numberBook = len(stack)-1
        
    # Display all data.
    print(" - - - - - - - - - - - - - - - - - - \n         Reading List Summary \n - - - - - - - - - - - - - - - - - - \n")
    print(" Current Book: " + currentRead)
    print(" Number of Books: "  + str(numberBook))
    print(" Books Read: " + str(numberRead))
    
    
# Getting values from initialisation.
[logPath, numberRead, stack] = init()

numberRead = 1
stack = "Attached"

main()

# Defining function to run at exit.
atexit.register(onClose, logPath, numberRead, stack)
