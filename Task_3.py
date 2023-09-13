# Quiz game using Tkinter in Python Programming.

import tkinter as tk
from tkinter import messagebox
app = tk.Tk()
app.title("Quiz Game")

questions = [
    "What is the capital of India?",
    "Who invent the number 'Zero' ?",
    "Who wrote the book 'Ramayana'?",
    "Most popular programming language in Data Science?"
]

answers = [
    "New Delhi","Aryabhatta","Valmiki","Python"
]

current_question = 0
def show_question():
    question_label.config(text=questions[current_question])
    answer_entry.delete(0, tk.END)

def check_answer():
    user_answer = answer_entry.get()
    correct_answer = answers[current_question]
    
    if user_answer.lower() == correct_answer.lower():
        messagebox.showinfo("Correct!", "Your answer is correct.")
    else:
        messagebox.showerror("Incorrect", f"Sorry, the correct answer is {correct_answer}.")
    
    next_question()

def next_question():
    global current_question
    current_question += 1
    if current_question < len(questions):
        show_question()
    else:
        messagebox.showinfo("Quiz Completed", "Congratulations, you have completed the quiz!")
        app.destroy()
        
question_label = tk.Label(app, text="", font=("Helvetica", 14))
question_label.pack(pady=20)

answer_entry = tk.Entry(app)
answer_entry.pack(pady=10)

submit_button = tk.Button(app, text="Submit Answer", command=check_answer).pack()

show_question()

next_question_button = tk.Button(app, text="Next Question", command=next_question).pack()

app.mainloop()
