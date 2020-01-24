import tkinter as tk
from tkinter import ttk
from tkinter import *
from configComp import configComp
import re


def openwindow2(root, results):
    x = []
    y = []
    result_window1 = tk.Toplevel(root)
    result_window1.title("CO2 Capture Results Graph")
    for key, value in results.items():
        y.append(value[1])
        x.append(key)
    print(x)
    print(y)
    
    
    sum = 0
    file = open('Halifax.txt', 'r')
    count, arr = 0, []
    for line in file.readlines():
        count += 1

        if count == 3:
            fname = line.rstrip().split(',')
            row = int(fname[0])
        if count == 4:
            fname = line.rstrip().split(',')
            column = int(fname[0])
        if count > 4:
            fname = line.rstrip().split(',') #using rstrip to remove the \n
            x = [(fname[i], fname[i+1]) for i in range(0, column*2, 2)]
            arr.append(x)

    text = [[None]*row for _ in range(column)]
    print([id(x) for x in text])

        # Get data from configComp


    for i in range(column):
        for j in range(row):
            colour = float(arr[j][i][0])
            number = colour
            if colour < 375: 
                colour = 'dark green'
            elif colour < 385:
                colour = 'green'
            elif colour < 395:
                colour = 'light green'
            elif colour <= 405:
                colour = 'yellow2'
            elif colour <= 415:
                colour = 'tomato'
            elif colour <= 420:
                colour = 'red'
            else:
                colour = 'red4'

            text[i][j] = Button(result_window1, text = number, bg = colour)
            text[i][j].config(textvariable = text[i][j], width = 9, height = 5)
            text[i][j].grid(column = i, row = j)



        