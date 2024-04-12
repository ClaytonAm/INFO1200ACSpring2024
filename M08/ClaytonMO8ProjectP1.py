#!/usr/bin/env python3

import tkinter as tk
from tkinter import ttk, messagebox 
import math as m

'''This calculator can take any 2 sides of the triangle and calculate the third side. 
I know it wasn't required, but I decided to have fun with it.'''

class overlyComplexTriangleCalculator(ttk.Frame):
    def __init__(self):
        #create the primary frame
        ttk.Frame.__init__(self, width=150, height=100, padding="10 10 10 10")

        #now initiate the components inside the frame
        self.initComponents()

    def initComponents(self):
        #tell the user to enter whichever sides they want
        ttk.Label(self, text="Enter 2 unknown sides").grid(columnspan=2, row=0, sticky=tk.EW)
        
        #declare the variables to be used later
        #sets default values to 0
        self.sideA = tk.IntVar(value=0)
        self.sideB = tk.IntVar(value=0)
        self.sideC = tk.IntVar(value=0)
        self.unknownSide = tk.IntVar()

        #make input fields
        self.createInputFields()
       
        #make the buttons
        self.makeButtons()

    def createInputFields(self):
         #these are just basic labels and entry fields
        ttk.Label(self, text="Side A:").grid(column=0, row=1, sticky=tk.E)
        ttk.Entry(self, width=10, textvariable=self.sideA).grid(column=1, row=1)
        
        ttk.Label(self, text="Side B:").grid(column=0, row=2, sticky=tk.E)
        ttk.Entry(self, width=10, textvariable=self.sideB).grid(column=1, row=2)
        
        ttk.Label(self, text="Side C:").grid(column=0, row=3, sticky=tk.E)
        ttk.Entry(self, width=10, textvariable=self.sideC).grid(column=1, row=3)
        
        #this is a read-only entry field to show the calculated answer
        ttk.Label(self, text="Unknown Side:").grid(column=0, row=5, sticky=tk.E)
        ttk.Entry(self, width=10, textvariable=self.unknownSide,state="readonly").grid(column=1, row=5)


    def makeButtons(self):
        #this function makes the buttons. Pretty self explanatory.
        buttonframe = ttk.Frame(self)
        buttonframe.grid(column=0, row=4, columnspan=2, sticky=tk.S)
        
        #this button does the actual calculations. First checks which of the sides were entered by the user.
        ttk.Button(buttonframe, text="Pythagorate!", command=lambda: self.comparator()).grid(column=0, row=0, sticky=tk.E)
        #this button just resets the values back to 0
        ttk.Button(buttonframe, text="Clear", command=lambda: self.resetFields()).grid(column=1, row=0, sticky=tk.W)
        
    def comparator(self):
        #this function checks which of the sides were entered by the user and routes it to the 
        #appropriate calculation.
        if self.sideC.get() == 0:
            self.unknownSide.set(self.calculateC())
        elif self.sideC.get() != 0:
            self.unknownSide.set(self.calculateAorB())
        else:
            print("Please enter something valid")

    def calculateC(self):
        #this function finds C if the user enters values for A and B
        self.unkSide = round(m.sqrt(self.sideA.get()**2 + self.sideB.get()**2), 3)
        return self.unkSide

    def calculateAorB(self):
        #this function checks whether A or B were left blank by the user
        #, then calculates the missing value
        if self.sideB.get() == 0:
            return round(m.sqrt(self.sideC.get()**2 - self.sideA.get()**2), 3)
        elif self.sideA.get() == 0:
            return round(m.sqrt(self.sideC.get()**2 - self.sideB.get()**2), 3)
        else:
            print("Something broke")

    def resetFields(self):
        #this function resets the fields back to 0
        self.sideA.set(0)
        self.sideB.set(0)
        self.sideC.set(0)
        self.unknownSide.set(0)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("The High Pot and Noose")
    overlyComplexTriangleCalculator().grid(row=0, column=0)
    root.mainloop()