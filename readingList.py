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
        
    return log, numberRead, stack

# Function to save data on close.
def onClose(log, numberRead, stack):
    
    # Writing data to log.
    log.write(numberRead, stack)
    
    # Saving log file.
    log.close()
    
# Main function.
def main():
    
    # Getting values from initialisation.
    [log, numberRead, stack] = init()
    
    # Defining function to run at exit.
    atexit(onClose(log, numberRead, stack))
    
main()

