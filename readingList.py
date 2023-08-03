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
        
    return logPath, numberRead, stack

# Function to save data on close.
def onClose():
    
    return 

# Main function.
def main():
    
    # Getting values from initialisation.
    [logPath, numberRead, stack] = init()
    

main()

# Defining function to run at exit.
atexit(onClose)