import tkinter as tk
from tkinter import messagebox

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")

        self.tasks = []

        # Configure colors and fonts
        self.bg_color = "#f0f0f0"  # Light gray background color
        self.button_color = "#4CAF50"  # Green button color
        self.hover_color = "#7FFF00"  # RGB effect color
        self.font = ("Arial", 12)

        # Main frame with light gray background
        self.main_frame = tk.Frame(root, bg=self.bg_color)
        self.main_frame.pack(padx=20, pady=20)

        # To-Do List label
        self.label_tasks = tk.Label(self.main_frame, text="To-Do List", font=("Arial", 18), bg=self.bg_color)
        self.label_tasks.pack(pady=10)

        # Task listbox with scrollbar
        self.task_listbox = tk.Listbox(self.main_frame, width=50, height=10, selectmode=tk.SINGLE, font=self.font)
        self.task_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.scrollbar = tk.Scrollbar(self.main_frame, orient=tk.VERTICAL, command=self.task_listbox.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.task_listbox.config(yscrollcommand=self.scrollbar.set)

        # Entry for new tasks
        self.entry = tk.Entry(root, width=52, font=self.font)
        self.entry.pack(pady=10)

        # Buttons with green background and white text
        self.add_button = tk.Button(root, text="Add Task", width=48, bg=self.button_color, fg="white", font=self.font, command=self.add_task)
        self.add_button.pack(pady=5)
        self.add_button.bind("<Enter>", lambda e: self.add_button.config(bg=self.hover_color))
        self.add_button.bind("<Leave>", lambda e: self.add_button.config(bg=self.button_color))

        self.remove_button = tk.Button(root, text="Remove Task", width=48, bg=self.button_color, fg="white", font=self.font, command=self.remove_task)
        self.remove_button.pack(pady=5)
        self.remove_button.bind("<Enter>", lambda e: self.remove_button.config(bg=self.hover_color))
        self.remove_button.bind("<Leave>", lambda e: self.remove_button.config(bg=self.button_color))

        self.view_button = tk.Button(root, text="View Tasks", width=48, bg=self.button_color, fg="white", font=self.font, command=self.view_tasks)
        self.view_button.pack(pady=5)
        self.view_button.bind("<Enter>", lambda e: self.view_button.config(bg=self.hover_color))
        self.view_button.bind("<Leave>", lambda e: self.view_button.config(bg=self.button_color))

        self.exit_button = tk.Button(root, text="Exit", width=48, bg=self.button_color, fg="white", font=self.font, command=root.quit)
        self.exit_button.pack(pady=5)
        self.exit_button.bind("<Enter>", lambda e: self.exit_button.config(bg=self.hover_color))
        self.exit_button.bind("<Leave>", lambda e: self.exit_button.config(bg=self.button_color))

    def add_task(self):
        task = self.entry.get()
        if task:
            self.tasks.append(task)
            self.entry.delete(0, tk.END)
            self.update_task_listbox()
            messagebox.showinfo("Task Added", "Task added successfully!")
        else:
            messagebox.showwarning("Input Error", "Please enter a task.")

    def remove_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            task_index = selected_task_index[0]
            self.tasks.pop(task_index)
            self.update_task_listbox()
            messagebox.showinfo("Task Removed", "Task removed successfully!")
        else:
            messagebox.showwarning("Selection Error", "Please select a task to remove.")

    def view_tasks(self):
        if not self.tasks:
            messagebox.showinfo("To-Do List", "Your to-do list is empty.")
        else:
            tasks_str = "\n".join(f"{idx + 1}. {task}" for idx, task in enumerate(self.tasks))
            messagebox.showinfo("To-Do List", tasks_str)

    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()
