import tkinter as tk
from tkinter import ttk
from tkinter import *


def openwindow(root):
    result_window = tk.Toplevel(root)
    result_window.title("CO2 Capture Results")

    # Labels
    result_window.l1 = tk.Label(result_window, text = "Money")
    result_window.l2 = tk.Label(result_window, text = "CO2 Saved")
    result_window.l3 = tk.Label(result_window, text = "City")
    result_window.l4 = tk.Label(result_window, text = "Placement of CSS")
    result_window.l1.grid(row=0, column=0, sticky=W)
    result_window.l2.grid(row=1, column=0, sticky=W)
    result_window.l3.grid(row=2, column=0, sticky=W)
    result_window.l4.grid(row=3, column=0, sticky=W)

    # Data labels
    result_window.d1 = tk.Label(result_window, text = 6)
    result_window.d2 = tk.Label(result_window, text = 8)
    result_window.d3 = tk.Label(result_window, text = 8)
    result_window.d4 = tk.Label(result_window, text = 1)
    result_window.d1.grid(row=0, column=2, sticky=W)
    result_window.d2.grid(row=1, column=2, sticky=W)
    result_window.d3.grid(row=2, column=2, sticky=W)
    result_window.d4.grid(row=3, column=2, sticky=W)

    # Set grid spacing
    col_count, row_count = result_window.grid_size()
    for col in range(col_count):
        result_window.grid_columnconfigure(col, minsize=100)

    for row in range(row_count):
        result_window.grid_rowconfigure(row, minsize=10)


