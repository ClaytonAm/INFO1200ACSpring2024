#!/usr/bin/env python3
import tkinter as tk
from tkinter import ttk, messagebox 
import math as m

class test_scores_GUI(ttk.Frame):
    def __init__(self):
        
        ttk.Frame.__init__(self, padding="10 10 10 10")

        self.init_components()

    def init_components(self):
        ttk.Label(self, text="Enter each test score").grid(column=1, row=0, sticky=tk.N)

        #declare the list of scores
        self.scores = []
        #declares an intermediate variable for the user inputted score
        self.score_input = tk.IntVar()

        #this is just declaring all the variables we'll use later
        #if I knew an elegant way to do this, I would already be asleep by now...
        self.scores_total = tk.IntVar()
        self.num_of_scores = tk.IntVar()
        self.average_score = tk.IntVar()
        self.low_score = tk.IntVar()
        self.high_score = tk.IntVar()
        self.median_score = tk.IntVar()

        self.build_scores_box()

        self.build_input_widgets()

        self.build_results_widgets()

    def input_scores(self):
        #this function grabs the value of the input box and adds it to the values in the listbox.
        #honestly kinda forgot how this worked after I made it 
        score_value = self.score_input.get()
        self.scores.append(score_value)
        
        self.scores_listbox.delete(0, tk.END)

        for score in self.scores:
            self.scores_listbox.insert(tk.END, score)
        
        self.score_input.set(0)

    def process_scores(self):
        #this is all of the nonsense to calculate the results of the inputted scores.
        #herein lies only pain and vapid repetition.
        self.scores.sort()
        self.scores_total.set(sum(self.scores))
        self.num_of_scores.set(len(self.scores))
        self.average_score.set(sum(self.scores) / len(self.scores))
        self.low_score.set(min(self.scores))
        self.high_score.set(max(self.scores))
        median_value = self.process_median()
        self.median_score.set(median_value)

    def process_median(self):
        median_index = (len(self.scores) // 2) - 1
        #checks if even
        if (len(self.scores) % 2) == 0:
            median_value = (self.scores[median_index] + self.scores[median_index + 1]) / 2
        #checks if the number of indexes is odd
        elif (len(self.scores) % 2) != 0:
            median_value = self.scores[median_index]
        return median_value
   
    def build_input_widgets(self):
        #this builds the widgets for the user's input
        ttk.Label(self, text="Score:").grid(column=0, row=1, sticky=tk.S)
        ttk.Entry(self, width=10, textvariable=self.score_input).grid(column=0, row=1)
        ttk.Button(self, text="Input", command= self.input_scores).grid(column=0, row=2)
        ttk.Button(self, text="Compute!", command=self.process_scores).grid(column=0, row=3)

    def build_scores_box(self):
        #this builds a frame to hold the inputted scores
        scores_frame = ttk.Frame(self)
        scores_frame.grid(column=0, row=4, rowspan=6)
        scores_label = ttk.Label(scores_frame, text="Scores:")
        scores_label.pack(side=tk.TOP, padx=5, pady=5)

        #this builds the box to hold all the user-entered scores
        scores_scrollbar = ttk.Scrollbar(scores_frame, orient=tk.VERTICAL)
        self.scores_listbox = tk.Listbox(scores_frame, yscrollcommand=scores_scrollbar.set)
        scores_scrollbar.config(command=self.scores_listbox.yview)
        scores_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.scores_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    def build_results_widgets(self):
        #this builds a frame to hold all the results
        results_frame = ttk.Frame(self)
        results_frame.grid(column=2, row=1, rowspan=7, sticky=tk.N)
        
        #these are all the labels and boxes holding the results. Forgot to make them read only but I'm lazy so oh well.
        #also there's gotta be a better way to do this lol
        ttk.Label(results_frame, text="Score Total:").grid(column=2, row=2, sticky=tk.E)
        ttk.Entry(results_frame, width=10, textvariable=self.scores_total).grid(column=3, row=2)

        ttk.Label(results_frame, text="Number of Scores:").grid(column=2, row=3, sticky=tk.E)
        ttk.Entry(results_frame, width=10, textvariable=self.num_of_scores).grid(column=3, row=3)

        ttk.Label(results_frame, text="Average Score:").grid(column=2, row=4, sticky=tk.E)
        ttk.Entry(results_frame, width=10, textvariable=self.average_score).grid(column=3, row=4)
        
        ttk.Label(results_frame, text="Low Score:").grid(column=2, row=5, sticky=tk.E)
        ttk.Entry(results_frame, width=10, textvariable=self.low_score).grid(column=3, row=5)

        ttk.Label(results_frame, text="High Score:").grid(column=2, row=6, sticky=tk.E)
        ttk.Entry(results_frame, width=10, textvariable=self.high_score).grid(column=3, row=6)

        ttk.Label(results_frame, text="Median Score:").grid(column=2, row=7, sticky=tk.E)
        ttk.Entry(results_frame, width=10, textvariable=self.median_score).grid(column=3, row=7)
        
#
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Test Scores GUI")
    test_scores_GUI().grid(row=0, column=0)
    root.mainloop()


