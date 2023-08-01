import tkinter as tk
from tkinter import messagebox
from math import *

def on_click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "C":
        entry.delete(0, tk.END)
    elif text == "π":
        entry.insert(tk.END, "pi")
    elif text == "e":
        entry.insert(tk.END, "e")
    elif text == "sin":
        entry.insert(tk.END, "sin(")
    elif text == "cos":
        entry.insert(tk.END, "cos(")
    elif text == "tan":
        entry.insert(tk.END, "tan(")
    elif text == "sqrt":
        entry.insert(tk.END, "sqrt(")
    elif text == "log":
        entry.insert(tk.END, "log(")
    elif text == "ln":
        entry.insert(tk.END, "log(")
    else:
        entry.insert(tk.END, text)

root = tk.Tk()
root.title("Scientific Calculator")

entry = tk.Entry(root, font=("Arial", 16), justify=tk.RIGHT)
entry.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

# Define the colors for the keys
key_bg_color = "black"
key_fg_color = "white"
equals_bg_color = "orange"
equals_fg_color = "black"

buttons = [
    ("C", "π", "e", "/", "sin"),
    ("7", "8", "9", "*", "cos"),
    ("4", "5", "6", "-", "tan"),
    ("1", "2", "3", "+", "sqrt"),
    ("0", ".", "(", ")", "log"),
    ("ln", "exp", "^", "!", "=")
]

for i, row in enumerate(buttons):
    for j, text in enumerate(row):
        bg_color = equals_bg_color if text == "=" else key_bg_color
        fg_color = equals_fg_color if text == "=" else key_fg_color
        button = tk.Button(root, text=text, font=("Arial", 16), width=5, height=2, bg=bg_color, fg=fg_color)
        button.grid(row=i+1, column=j, padx=5, pady=5)
        button.bind("<Button-1>", on_click)

root.bind("<Return>", on_click)  # Bind Enter key to "="
root.bind("<Escape>", lambda event: on_click(event, text="C"))  # Bind Escape key to "C"

# Bind numeric keys and operators to the corresponding buttons
root.bind("0", lambda event: on_click(event, text="0"))
root.bind("1", lambda event: on_click(event, text="1"))
root.bind("2", lambda event: on_click(event, text="2"))
root.bind("3", lambda event: on_click(event, text="3"))
root.bind("4", lambda event: on_click(event, text="4"))
root.bind("5", lambda event: on_click(event, text="5"))
root.bind("6", lambda event: on_click(event, text="6"))
root.bind("7", lambda event: on_click(event, text="7"))
root.bind("8", lambda event: on_click(event, text="8"))
root.bind("9", lambda event: on_click(event, text="9"))
root.bind("+", lambda event: on_click(event, text="+"))
root.bind("-", lambda event: on_click(event, text="-"))
root.bind("*", lambda event: on_click(event, text="*"))
root.bind("/", lambda event: on_click(event, text="/"))
root.bind(".", lambda event: on_click(event, text="."))
root.bind("^", lambda event: on_click(event, text="**"))

root.mainloop()
