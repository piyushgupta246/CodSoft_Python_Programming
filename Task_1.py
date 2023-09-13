# Create a To-Do List by using tkinter in Python Programming.

import tkinter as tk
from tkinter import messagebox
a=tk.Tk()
a.title("To-Do List App")
def Add():
    task = task_entry.get()
    if task:
        task_list.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")
def Remove():
    selected_task = task_list.curselection()
    if selected_task:
        task_list.delete(selected_task)
    else:
        messagebox.showwarning("Warning", "Please select a task to remove.")
        
task_entry = tk.Entry(a, width=40)
task_entry.pack(pady=10)

add_button = tk.Button(a, text="Add", command=Add).pack()

remove_button = tk.Button(a, text="Remove", command=Remove).pack()

task_list = tk.Listbox(a, selectmode=tk.SINGLE, width=40, height=10)
task_list.pack(pady=10)

a.mainloop()
