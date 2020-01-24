#! ./env/bin/python3

# Author: Ben Myles
# Originally written 2019-05-23
# Modified for AEC on 2020-10-24

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
import os
from readfile import readfile

class Schedule:

    def __init__(self, master):
        self.master = master
        master.title("CO2 Capture Optimization")
        master.geometry("800x600+200+150")

        # Instance variables
        self.term = StringVar()
        self.location = StringVar()
        self.term_selected = False
        self.location_selected = False
        self.filenames = set()

        # Instructions label
        self.term_lbl = Label(master, text="Please select input files for cities")
        self.term_lbl.grid(row=1, column=1, sticky=W)

        # Output text area
        self.output = Text(master, height=10, width=30, yscrollcommand=set(), highlightbackground="black", highlightthickness=5)
        self.output.grid(row=2, column=1, rowspan=2, columnspan=1)
        self.output.config(state=DISABLED)

        # "Add" button
        self.add_butt = ttk.Button(master, text="Add", command=self.add)
        self.add_butt.grid(row=2, column=2, sticky=W)

        # "Done" button
        self.done_butt = ttk.Button(master, text="Done", command=self.done)
        self.done_butt.grid(row=3, column=2, sticky=W)

        # Set grid spacing
        col_count, row_count = master.grid_size()
        for col in range(col_count):
            master.grid_columnconfigure(col, minsize=10)

        for row in range(row_count):
            master.grid_rowconfigure(row, minsize=10)

    def output_text(self, out):
        self.output.config(state=NORMAL)
        self.output.insert(END, out)
        self.output.config(state=DISABLED)

    def trim_filename(self, path):
        return os.path.basename(path)

    def done(self):
        for file in self.filenames:
            readfile(file)

    def add(self):
        # Button has been pressed
        filename = askopenfilename()
        if filename not in self.filenames:
            self.filenames.add(filename)
            self.output_text(self.trim_filename(filename))
            self.output_text("\n")
        else:
            messagebox.showerror("Error", "File has already been added")

root = Tk()
#root.attributes('-zoomed', True)
gui = Schedule(root)
root.mainloop()
