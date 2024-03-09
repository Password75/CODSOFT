import tkinter as tk

class TodoApp:
    def __init__(self, master):
        self.master = master
        self.master.title("To-Do List App")
        self.master.configure(bg="black")
        
        self.tasks = []

        self.task_var = tk.StringVar()
        
        # Entry widget to enter tasks
        self.task_entry = tk.Entry(master, textvariable=self.task_var, width=30, font=("Arial", 12))
        self.task_entry.grid(row=0, column=0, padx=5, pady=5, columnspan=2)
        
        # Button to add tasks
        add_button = tk.Button(master, text="Add Task", command=self.add_task, bg="black", fg="white", relief=tk.RIDGE, font=("Arial", 12), bd=3)
        add_button.grid(row=0, column=2, padx=5, pady=5)
        
        # Listbox to display tasks
        self.task_listbox = tk.Listbox(master, width=40, height=10, font=("Arial", 12), bg="white", fg="black")
        self.task_listbox.grid(row=1, column=0, columnspan=3, padx=5, pady=5)
        
        # Button to delete selected task
        delete_button = tk.Button(master, text="Delete Task", command=self.delete_task, bg="black", fg="white", relief=tk.RIDGE, font=("Arial", 12), bd=3)
        delete_button.grid(row=2, column=0, padx=5, pady=5)
        
        # Button to clear all tasks
        clear_button = tk.Button(master, text="Clear All", command=self.clear_tasks, bg="black", fg="white", relief=tk.RIDGE, font=("Arial", 12), bd=3)
        clear_button.grid(row=2, column=1, padx=5, pady=5)

    def add_task(self):
        task = self.task_var.get()
        if task:
            self.tasks.append(task)
            self.task_listbox.insert(tk.END, task)
            self.task_var.set("")
        else:
            self.display_error("Please enter a task!")

    def delete_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            self.task_listbox.delete(selected_index)
            del self.tasks[selected_index]
        except IndexError:
            self.display_error("Please select a task to delete!")

    def clear_tasks(self):
        self.task_listbox.delete(0, tk.END)
        self.tasks.clear()

    def display_error(self, message):
        error_label = tk.Label(self.master, text=message, fg="red")
        error_label.grid(row=3, column=0, columnspan=3, padx=5, pady=5)

def main():
    root = tk.Tk()
    root.configure(bg="black")
    app = TodoApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
