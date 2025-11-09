import tkinter as tk
from tkinter import messagebox
import math

root = tk.Tk()
root.title("Scientific Calculator")
root.geometry("400x600")  # slightly bigger to fit extra buttons
root.resizable(False, False)

entry = tk.Entry(root, width=20, font=("Arial", 24), borderwidth=2, relief="ridge")
entry.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

def click(button_text):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + button_text)

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        expr = entry.get()
        expr = expr.replace("^", "**")  # support exponentiation
        result = eval(expr, {"__builtins__": None}, math.__dict__)
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception:
        messagebox.showerror("Error", "Invalid Input")

def sqrt():
    try:
        value = float(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(math.sqrt(value)))
    except Exception:
        messagebox.showerror("Error", "Invalid Input")

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3), ('C', 1, 4),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3), ('(', 2, 4),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3), (')', 3, 4),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('^', 4, 3), ('=', 4, 4)
]

for (text, row, col) in buttons:
    if text == "=":
        btn = tk.Button(root, text=text, width=5, height=2, font=("Arial", 16), command=calculate)
    elif text == "C":
        btn = tk.Button(root, text=text, width=5, height=2, font=("Arial", 16), command=clear)
    else:
        btn = tk.Button(root, text=text, width=5, height=2, font=("Arial", 16),
                        command=lambda t=text: click(t))
    btn.grid(row=row, column=col, padx=5, pady=5)

sci_buttons = [
    ('sin', 5, 0), ('cos', 5, 1), ('tan', 5, 2),
    ('log', 5, 3), ('sqrt', 5, 4)
]

for (text, row, col) in sci_buttons:
    if text == "sqrt":
        btn = tk.Button(root, text=text, width=5, height=2, font=("Arial", 16), command=sqrt)
    else:
        btn = tk.Button(root, text=text, width=5, height=2, font=("Arial", 16),
                        command=lambda t=text: click(t + "("))
    btn.grid(row=row, column=col, padx=5, pady=5)

root.mainloop()
