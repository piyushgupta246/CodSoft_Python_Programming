# Create a Calculator by using tkinter in Python Programming.

import tkinter as tk

def Click(number):
    current = display.get()
    display.delete(0, tk.END)
    display.insert(tk.END, current + str(number))

def Clear():
    display.delete(0, tk.END)

def Equal():
    try:
        expression = display.get()
        result = eval(expression)
        display.delete(0, tk.END)
        display.insert(tk.END, result)
    except:
        display.delete(0, tk.END)
        display.insert(tk.END, "Error")

root = tk.Tk()
root.title("Calculator")

display = tk.Entry(root, width=25, justify=tk.RIGHT)
display.grid(row=0, column=0, columnspan=4)

button_1 = tk.Button(root,text="1", command=lambda: Click(1)).grid(row=1, column=0)

button_2 = tk.Button(root,text="2", command=lambda: Click(2)).grid(row=1, column=1)

button_3 = tk.Button(root,text="3", command=lambda: Click(3)).grid(row=1, column=2)

button_4 = tk.Button(root,text="4", command=lambda: Click(4)).grid(row=2, column=0)

button_5 = tk.Button(root,text="5", command=lambda: Click(5)).grid(row=2, column=1)

button_6 = tk.Button(root,text="6", command=lambda: Click(6)).grid(row=2, column=2)

button_7 = tk.Button(root,text="7", command=lambda: Click(7)).grid(row=3, column=0)

button_8 = tk.Button(root,text="8", command=lambda: Click(8)).grid(row=3, column=1)

button_9 = tk.Button(root,text="9", command=lambda: Click(9)).grid(row=3, column=2)

button_0 = tk.Button(root,text="0", command=lambda: Click(0)).grid(row=4, column=1)

button_plus = tk.Button(root,text="+", command=lambda: Click("+")).grid(row=1, column=3)

button_minus = tk.Button(root,text="-", command=lambda: Click("-")).grid(row=2, column=3)

button_multiply = tk.Button(root,text="*", command=lambda: Click("*")).grid(row=3, column=3)

button_divide = tk.Button(root,text="/", command=lambda: Click("/")).grid(row=4, column=3)

button_equal = tk.Button(root,text="=", command=Equal).grid(row=4, column=2)

button_clear = tk.Button(root,text="C", command=Clear).grid(row=4, column=0)

root.mainloop()
