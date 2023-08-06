# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 08:13:28 2023

@author: hnewey7
"""

import sys
import os
import pandas
import keyboard
import time

# - - - - - - - - - - - - - - - - - - - - - 
# Initialisation function.
def init():
    # Getting file location.
    logPath = getLog()
    
    # Getting data from csv file.
    [numberRead, stack, currentRead, numberBook] = getData(logPath)
    
    return numberRead, stack, currentRead, numberBook, logPath

# Get log function
def getLog():
    # Getting events log path.
    folderPath = os.path.dirname(os.path.abspath(sys.argv[0]))
    logPath = folderPath + "\\log.csv"
    
    return logPath

# Get data function.
def getData(logPath):
    
    # Evaluating if logPath exists.
    if os.path.exists(logPath):
        # Reading data from csv file.
        data = pandas.read_csv(logPath)
        datalist = data['log'].values.tolist()
    
        # Extracting stats from data.
        numberRead = int(datalist[0])
        stack = datalist[1:len(datalist)]
        
        # Evaluating statistics depending on length of stack.
        if len(stack)>0:
            currentRead = stack[len(stack)-1]
            numberBook = len(stack)
        else:
            currentRead = "Not reading anything."
            numberBook = 0
    else:
        # Setting default stats.
        numberRead = 0
        stack = []
        currentRead = "Not reading anything."
        numberBook = 0
        
    return numberRead, stack, currentRead, numberBook

# - - - - - - - - - - - - - - - - - - - - - 
# Main function.
def main(numberRead, stack, currentRead, numberBook, logPath):
    # Displaying statistics for user.
    displayStats(numberRead, stack, currentRead, numberBook)
    
    # Prompt user for command input
    userCommand = promptInput()
    
    # Evaluate user input.
    [numberRead, stack] = evalInput(userCommand, numberRead, stack)
    
    # Saving data.
    saveData(numberRead, stack, logPath)
    
    # Exiting script.
    if userCommand == "Exit":
        os._exit(0)
        
# Function for displaying stats.
def displayStats(numberRead, stack, currentRead, numberBook):
    
    print(" - - - - - - - - - - - - - - - - - - \n        Reading List Summary: \n - - - - - - - - - - - - - - - - - -")
    print("Currently Reading: " + str(currentRead))
    print("Number of Books to Read: " + str(numberBook))
    print("Books Read: " + str(numberRead))
    print(" - - - - - - - - - - - - - - - - - - ")

# Function to prompt user input.
def promptInput():
    
    # Prompting user input.
    userCommand = print("Select your input: [Add(a)/Completed(c)/Exit(e)] ")
    
    # Waiting for user input.
    while True:
        if keyboard.is_pressed('a'):
            userCommand = "Add"
            keyboard.send("backspace")
            break
        elif keyboard.is_pressed('c'):
            userCommand = "Completed"
            keyboard.send("backspace")
            break
        elif keyboard.is_pressed('e'):
            userCommand = "Exit"
            keyboard.send("backspace")
            break
    
    # Wait for 0.5 seconds.
    time.sleep(0.5)
    
    return userCommand

# Function for evaluating the user input.
def evalInput(userCommand, numberRead, stack):

    # Evaluating userCommand.
    if userCommand == "Add":
        # Prompt user to add another book and adding to stack.
        newBook = input("Enter new book: ")
        stack.append(newBook)
    elif userCommand == "Completed":
        # Evaluating whether can be completed.
        if len(stack)>0: 
            # Adding one to count.
            numberRead = numberRead + 1
            # Remove last item from stack.
            stack.pop()
        else:
            print("Reading list is currently empty.")
            time.sleep(2)
            
    return numberRead, stack

# Function for saving data.
def saveData(numberRead, stack, logPath):
    # Creating datalist.
    datalist = []
    
    #Appending datalist with data.
    datalist.append("log")
    datalist.append(numberRead)
    for item in stack:
        datalist.append(item)
    
    # Creating dataframe from datalist.
    dataframe = pandas.DataFrame(datalist)
    
    # Converting to csv file.
    dataframe.to_csv(logPath, header=None, index=None)
    
# - - - - - - - - - - - - - - - - - - - - - 

# Looping function.
def loop():
    # Initialisation.
    [numberRead, stack, currentRead, numberBook, logPath] = init()
    
    # Main.
    main(numberRead, stack, currentRead, numberBook, logPath)
    
    # Clearing terminal.
    os.system('cls')
    
    # Loop.
    loop()
    
# - - - - - - - - - - - - - - - - - - - - - 

loop()