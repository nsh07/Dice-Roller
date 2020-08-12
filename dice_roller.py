# Super simple dice roll program
# Fun fact: this program has only 11 lines of code!

import random
import tkinter as tk

root=tk.Tk()
root.title("Dice Roller")

def coin_toss():
    tk.Label(text=random.choice(("Head", "Tail"))).grid(row=1, column=1, sticky="EW")

def dice_roll():
    tk.Label(text=random.randint(1, 6)).grid(row=1, column=2, sticky="EW")

tk.Button(text="Toss Coin", command=coin_toss).grid(row=2, column=1, sticky="NSEW")
tk.Button(text="Roll Dice", command=dice_roll).grid(row=2, column=2, sticky="NSEW")
root.mainloop()
