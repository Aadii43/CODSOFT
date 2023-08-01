import tkinter as tk
from tkinter import messagebox
import random

# Quiz questions and answers
quiz_questions = [
    {
        "question": "What is the capital of France?",
        "options": ["London", "Paris", "Berlin", "Rome"],
        "correct_answer": "Paris"
    },
    {
        "question": "Which planet is closest to the Sun?",
        "options": ["Mars", "Venus", "Mercury", "Earth"],
        "correct_answer": "Mercury"
    },
    {
        "question": "Who painted the Mona Lisa?",
        "options": ["Pablo Picasso", "Vincent van Gogh", "Leonardo da Vinci", "Michelangelo"],
        "correct_answer": "Leonardo da Vinci"
    }
]

class QuizGameApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Quiz Game")
        self.geometry("500x300")
        self.score = 0
        self.current_question_index = 0

        self.label_question = tk.Label(self, text="", wraplength=400, font=("Arial", 12))
        self.label_question.pack(pady=10)

        self.var_answer = tk.StringVar()
        self.var_answer.set(None)

        self.radio_buttons = []
        for i in range(4):
            rb = tk.Radiobutton(self, text="", variable=self.var_answer, value=i, font=("Arial", 10))
            rb.pack(anchor="w")
            self.radio_buttons.append(rb)

        self.button_submit = tk.Button(self, text="Submit", command=self.submit_answer)
        self.button_submit.pack(pady=10)

        self.load_question()
        self.mainloop()

    def load_question(self):
        if self.current_question_index < len(quiz_questions):
            question = quiz_questions[self.current_question_index]
            self.label_question.config(text=question["question"])

            for i in range(4):
                self.radio_buttons[i].config(text=question["options"][i])

    def submit_answer(self):
        if self.var_answer.get() is not None:
            question = quiz_questions[self.current_question_index]
            selected_answer = question["options"][int(self.var_answer.get())]
            correct_answer = question["correct_answer"]

            if selected_answer == correct_answer:
                self.score += 1
                messagebox.showinfo("Result", "Correct!")
            else:
                messagebox.showinfo("Result", f"Incorrect!\nThe correct answer is: {correct_answer}")

            self.current_question_index += 1
            self.var_answer.set(None)
            self.load_question()
        else:
            messagebox.showwarning("Warning", "Please select an answer!")

        if self.current_question_index == len(quiz_questions):
            self.display_final_results()

    def display_final_results(self):
        final_score = (self.score / len(quiz_questions)) * 100
        if final_score == 100:
            performance_message = "Congratulations! You got all the answers correct."
        elif final_score >= 70:
            performance_message = "Good job! You did well."
        else:
            performance_message = "You can do better. Keep practicing!"

        messagebox.showinfo("Final Results", f"Your score: {final_score:.2f}%\n{performance_message}")

        play_again = messagebox.askyesno("Play Again", "Do you want to play again?")
        if play_again:
            self.score = 0
            self.current_question_index = 0
            self.load_question()
        else:
            self.destroy()

if __name__ == "__main__":
    app = QuizGameApp()
