import tkinter as tk
from tkinter import messagebox
from tkinter import font
from datetime import datetime
from collections import deque

def add_task():
    task = entry.get()
    category = entry_category.get()
    priority = entry_priority.get()

    if task and category and priority.isdigit():
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        task_with_time = f"{task} (Added on: {current_time})"
        task_details = {
            'task': task_with_time,
            'category': category,
            'priority': int(priority)
        }
        tasks.append(task_with_time)
        task_details_dict[task_with_time] = task_details
        task_deque.appendleft(task_with_time)
        categories.add(category)
        task_listbox.insert(tk.END, task_with_time)
        entry.delete(0, tk.END)
        entry_category.delete(0, tk.END)
        entry_priority.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task, category, and valid priority")

def remove_task():
    selected_task_index = task_listbox.curselection()
    if selected_task_index:
        index = selected_task_index[0]
        task = tasks[index]
        del tasks[index]
        del task_details_dict[task]
        task_deque.remove(task)
        task_listbox.delete(index)
    else:
        messagebox.showwarning("Warning", "Please select a task to remove")

def sort_tasks():
    tasks.sort()
    refresh_listbox()

def refresh_listbox():
    task_listbox.delete(0, tk.END)
    for task in tasks:
        task_listbox.insert(tk.END, task)

def toggle_task_completion():
    selected_task_index = task_listbox.curselection()
    if selected_task_index:
        index = selected_task_index[0]
        task = tasks[index]
        if task.startswith("• "):
            task = task[2:]
        else:
            task = "• " + task
        tasks[index] = task
        refresh_listbox()
    else:
        messagebox.showwarning("Warning", "Please select a task to mark as completed")

def search_task():
    query = entry_search.get().lower()
    search_result = []
    for task in tasks:
        if query in task.lower():
            search_result.append(task)
    refresh_search_listbox(search_result)

def refresh_search_listbox(search_result):
    search_listbox.delete(0, tk.END)
    for task in search_result:
        search_listbox.insert(tk.END, task)

root = tk.Tk()
root.title("To-do List")
root.geometry("600x500")

custom_font = font.Font(family="TkDefaultFont", size=14)
entry = tk.Entry(root, font=custom_font, width=50)
entry.pack(pady=10)

entry_category = tk.Entry(root, font=custom_font, width=20)
entry_category.pack(pady=10)

entry_priority = tk.Entry(root, font=custom_font, width=10)
entry_priority.pack(pady=10)

add_button = tk.Button(root, text="Add Task", font=custom_font, command=add_task)
remove_button = tk.Button(root, text="Remove Task", font=custom_font, command=remove_task)
sort_button = tk.Button(root, text="Sort Tasks", font=custom_font, command=sort_tasks)
toggle_button = tk.Button(root, text="Toggle Complete", font=custom_font, command=toggle_task_completion)

add_button.pack(side=tk.LEFT, padx=5)
remove_button.pack(side=tk.LEFT, padx=5)
sort_button.pack(side=tk.LEFT, padx=5)
toggle_button.pack(side=tk.LEFT, padx=5)

tasks = []
task_details_dict = {}
categories = set()
task_deque = deque()
task_listbox = tk.Listbox(root, font=custom_font, selectmode=tk.SINGLE, width=50, height=10)
task_listbox.pack(pady=10, padx=10)

search_frame = tk.Frame(root)
search_frame.pack(pady=10)

entry_search = tk.Entry(search_frame, font=custom_font, width=30)
entry_search.pack(side=tk.LEFT, padx=5)

search_button = tk.Button(search_frame, text="Search", font=custom_font, command=search_task)
search_button.pack(side=tk.LEFT, padx=5)

search_listbox = tk.Listbox(root, font=custom_font, selectmode=tk.SINGLE, width=50, height=5)
search_listbox.pack(pady=10, padx=10)

root.mainloop()
