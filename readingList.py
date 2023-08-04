# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 08:13:28 2023

@author: hnewey7
"""

# Initialisation function.
def init():
    # Getting data from csv file.
    [numberRead, stack] = getData()
    
# Main function.
def main():
    # Displaying statistics for user.
    displayStats(numberRead, stack)
    
    # Prompt user for command input
    userCommand = promptInput()
    
    # Evaluate user input.
    [numberRead, stack] = evalInput(userCommand)
    
# On close function.
def onClose():
    # Saving data.
    saveData(numberRead, stack)
    
init()
main()
onClose()