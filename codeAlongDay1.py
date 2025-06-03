# Tkinter Advanced Widgets
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Code Along Day 1")
root.geometry("300x200")
# Force window to be on top
root.attributes('-topmost', True)

name_var = tk.StringVar()
greet_var = tk.StringVar(value="Hello, future programmer!")

#input field
entry_label = ttk.Label(root, text="Enter your name:")
entry_label.pack(pady=5, padx=5)

name_entry = ttk.Entry(root, textvariable=name_var)
name_entry.pack(pady=5, padx=5)

#output label
greet_label = ttk.Label(root, textvariable=greet_var)
greet_label.pack(pady=5, padx=5)

#define a function to update the greeting
def greet():
    name = name_var.get()
    if name:
        greet_var.set(f"Hello, {name}!")
    else:
        greet_var.set("Hello, future programmer!")
        
#button to trigger the greeting
greet_button = ttk.Button(root, text="Greet", command=greet)
greet_button.pack(pady=5, padx=5)

#button to close the application
close_button = ttk.Button(root, text="Close", command=root.destroy)
close_button.pack(pady=5, padx=5)

# Run the application
root.mainloop()
# This code creates a simple Tkinter application with an entry field, a greeting label, and buttons to greet the user or close the application.


