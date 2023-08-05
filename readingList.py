# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 08:13:28 2023

@author: hnewey7
"""

import os
import pandas

# - - - - - - - - - - - - - - - - - - - - - 
# Initialisation function.
def init():
    # Getting file location.
    logPath = getLog()
    
    # Getting data from csv file.
    [numberRead, stack] = getData(logPath)
    
    return numberRead, stack

# Get log function
def getLog():
    # Getting events log path.
    folderPath = os.path.dirname(os.path.abspath(__file__))
    logPath = folderPath + "\\test.csv"
    
    return logPath

# Get data function.
def getData(logPath):
    # Reading data from csv file.
    data = pandas.read_csv(logPath)
    datalist = data["log"].tolist()
    
    # Extracting stats from data.
    numberRead = datalist[0]
    stack = datalist[1:len(datalist)]

    return numberRead, stack

# - - - - - - - - - - - - - - - - - - - - - 
# Main function.
#def main():
#    # Displaying statistics for user.
#    displayStats(numberRead, stack)
#    
#    # Prompt user for command input
#    userCommand = promptInput()
#    
#    # Evaluate user input.
#    [numberRead, stack] = evalInput(userCommand)
#    
# - - - - - - - - - - - - - - - - - - - - - 
# On close function.
#def onClose():
#    # Saving data.
#    saveData(numberRead, stack)
#    
init()
#main()
#onClose()