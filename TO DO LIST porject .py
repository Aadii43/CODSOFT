import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import random

tasks = []

def create_task():
    task = task_entry.get()
    if task:
        current_date = datetime.now().strftime("%d/%m/%Y")
        task_with_date = f"{task} ({current_date})"
        tasks.append(task_with_date)
        task_list.insert(tk.END, task_with_date)
        task_entry.delete(0, tk.END)
        messagebox.showinfo("Task Created", "Task created successfully!")
    else:
        messagebox.showwarning("Empty Task", "Please enter a task.")

def update_task():
    selected_index = task_list.curselection()
    if selected_index:
        task_number = selected_index[0]
        new_task = task_entry.get()
        if new_task:
            current_date = datetime.now().strftime("%d/%m/%Y")
            task_with_date = f"{new_task} ({current_date})"
            tasks[task_number] = task_with_date
            task_list.delete(selected_index)
            task_list.insert(selected_index, task_with_date)
            task_entry.delete(0, tk.END)
            messagebox.showinfo("Task Updated", "Task updated successfully!")
        else:
            messagebox.showwarning("Empty Task", "Please enter a task.")
    else:
        messagebox.showwarning("No Task Selected", "Please select a task to update.")

def delete_task():
    selected_index = task_list.curselection()
    if selected_index:
        task_number = selected_index[0]
        task_list.delete(selected_index)
        deleted_task = tasks.pop(task_number)
        messagebox.showinfo("Task Deleted", f"Task '{deleted_task}' has been deleted.")
    else:
        messagebox.showwarning("No Task Selected", "Please select a task to delete.")

def update_datetime_label():
    current_datetime = datetime.now().strftime("%H:%M:%S")
    current_date = datetime.now().strftime("%d/%m/%Y")
    datetime_label.config(text=f"{current_datetime}\n{current_date}")
    datetime_label.after(1000, update_datetime_label)

def apply_theme(theme):
    root.configure(bg=theme["bg_color"])
    heading_label.config(bg=theme["bg_color"], fg=theme["fg_color"], font=theme["font"])
    add_button.config(bg=theme["bg_color"], fg=theme["fg_color"], font=theme["font"])
    update_button.config(bg=theme["bg_color"], fg=theme["fg_color"], font=theme["font"])
    delete_button.config(bg=theme["bg_color"], fg=theme["fg_color"], font=theme["font"])
    task_list.config(bg=theme["bg_color"], fg=theme["fg_color"], font=theme["font"])
    datetime_label.config(bg=theme["bg_color"], fg=theme["fg_color"], font=theme["font"])

def change_theme():
    themes = [
        {"bg_color": "lightblue", "fg_color": "black", "font": ("Arial", 12)},
        {"bg_color": "lightgreen", "fg_color": "white", "font": ("Helvetica", 14, "bold")},
        {"bg_color": "lightyellow", "fg_color": "blue", "font": ("Times New Roman", 12, "italic")},
        {"bg_color": "lightpink", "fg_color": "purple", "font": ("Courier New", 12, "underline")},
    ]
    random_theme = random.choice(themes)
    apply_theme(random_theme)

root = tk.Tk()
root.title("To-Do List")

# Create Heading Label
heading_label = tk.Label(root, text="TO DO LIST", font=("Arial Bold", 16))
heading_label.pack(pady=10)

# Create Task Entry
task_entry = tk.Entry(root, font=("Arial", 12))
task_entry.pack(pady=5)

# Create Add Task Button
add_button = tk.Button(root, text="Add Task", font=("Arial", 12), command=create_task)
add_button.pack(pady=5)

# Create Task List
task_list = tk.Listbox(root, width=50, height=10, font=("Arial", 12))
task_list.pack(padx=10, pady=10)

# Create Update Button
update_button = tk.Button(root, text="Update", font=("Arial", 12), command=update_task)
update_button.pack(pady=5)

# Create Delete Button
delete_button = tk.Button(root, text="Delete", font=("Arial", 12), command=delete_task)
delete_button.pack(pady=5)

# Create Date and Time Display
datetime_label = tk.Label(root, text="", font=("Arial", 12), anchor=tk.SE)
datetime_label.pack(side=tk.RIGHT, padx=10, pady=10)
update_datetime_label()

# Create Change Theme Button
theme_button = tk.Button(root, text="Change Theme", font=("Arial", 12), command=change_theme)
theme_button.pack(side=tk.LEFT, padx=10, pady=10)

root.mainloop()
