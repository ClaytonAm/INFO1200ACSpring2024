import requests
import tkinter as tk
from tkinter import ttk, messagebox, filedialog


def __init__(self):
    ttk.Frame.__init__(self, )
    
    self.ability_scores = {
        "Strength": tk.IntVar(value=10),
        "Dexterity": tk.IntVar(value=10),
        "Constitution": tk.IntVar(value=10),
        "Intelligence": tk.IntVar(value=10),
        "Wisdom": tk.IntVar(value=10),
        "Charisma": tk.IntVar(value=10),
    }

    self.init_components()

def init_components(self):
    
    self.build_top_bar()

    self.build_ability_score_frames()

def build_top_bar(self):
    top_bar_frame = ttk.Frame(self)
    top_bar_frame.grid(columnspan=5, row=0)
    

def build_ability_score_frames(self):
    ability_Scores_Frame = ttk.Frame(self, borderwidth=2, relief="groove")
    ability_Scores_Frame.grid(column=0, row=3, padx=15, sticky="ew")

    row = 1
    for ability, score in self.ability_scores.items():
        frame = ttk.Frame(self, borderwidth=2, relief="ridge")
        frame.grid(row=row, column=0, columnspan=2, padx=5, pady=5, sticky="ew")

        ttk.Label(frame, text=ability).grid(row=0, column=0, padx=5, pady=5, sticky="ew")
        score_entry = tk.Entry(frame, textvariable=score, width=5)
        score_entry.grid(row=1, sticky="ew")
        modifier_entry = tk.Entry(frame, textvariable=self.calc_Mod(score), width=5, state="readonly")
        modifier_entry.grid(row=2, sticky="ew")
        
        row += 1


def calc_Mod(self, abilityScore):
    possible_ability_scores = [0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30]
    modifiers_list = [-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10]

    score_value = abilityScore.get()
    if score_value % 2 == 0:
        i = possible_ability_scores.index(score_value)
        modifier = modifiers_list[i]
    else:
        value = score_value - 1
        i = possible_ability_scores.index(value)
        modifier = modifiers_list[i]
    return modifier

def read_ability_scores():
    pass
def calc_Proficiency():
    pass
def calc_AC():
    pass




root = tk.Tk()
root.title("Character Sheet")




root.mainloop()

