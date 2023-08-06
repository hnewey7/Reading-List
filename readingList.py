# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 08:13:28 2023

@author: hnewey7
"""

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
    folderPath = os.path.dirname(os.path.abspath(__file__))
    logPath = folderPath + "\\test.csv"
    
    return logPath

# Get data function.
def getData(logPath):
    # Reading data from csv file.
    data = pandas.read_csv(logPath)
    print(data)
    datalist = data['log'].values.tolist()
    print(datalist)
    # Extracting stats from data.
    numberRead = datalist[0]
    stack = datalist[1:len(datalist)]
    currentRead = stack[len(stack)-1]
    numberBook = len(stack)
    
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
    print(stack)
    # Evaluating userCommand.
    if userCommand == "Add":
        # Prompt user to add another book and adding to stack.
        newBook = input("Enter new book: ")
        stack.append(newBook)
    elif userCommand == "Completed":
        # Remove last item from stack.
        stack.pop()
        print(stack)
        
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
    #os.system('cls')
    
    # Loop.
    loop()
    
# - - - - - - - - - - - - - - - - - - - - - 

loop()