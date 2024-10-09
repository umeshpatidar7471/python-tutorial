import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry_task.get()
    if task != "":
        listbox_tasks.insert(tk.END, task)
        entry_task.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def delete_task():
    try:
        task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(task_index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete.")

# Create main window
root = tk.Tk()
root.title("To-Do List")

# Create frames
frame_tasks = tk.Frame(root)
frame_tasks.pack(pady=10)

# Create listbox
listbox_tasks = tk.Listbox(frame_tasks, height=15, width=50)
listbox_tasks.pack(side=tk.LEFT)

# Create scrollbar
scrollbar_tasks = tk.Scrollbar(frame_tasks)
scrollbar_tasks.pack(side=tk.RIGHT, fill=tk.Y)

# Connect scrollbar to listbox
listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox_tasks.yview)

# Create entry widget
entry_task = tk.Entry(root, width=50)
entry_task.pack(pady=10)

# Create buttons
button_add_task = tk.Button(root, text="Add Task", width=48, command=add_task)
button_add_task.pack()

button_delete_task = tk.Button(root, text="Delete Task", width=48, command=delete_task)
button_delete_task.pack()

# Run the application
root.mainloop()