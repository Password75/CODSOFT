import tkinter as tk
from tkinter import messagebox
import random
import string

class PasswordGeneratorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Password Generator")
        self.master.configure(bg="#f0f0f0")

        # Frame to hold widgets
        self.frame = tk.Frame(master, padx=50, pady=50, bg="#f0f0f0")
        self.frame.pack()

        # Label and Entry for password length
        self.length_label = tk.Label(self.frame, text="Password Length:", font=("Arial", 16), bg="#f0f0f0")
        self.length_label.grid(row=0, column=0, padx=5, pady=5)

        self.length_entry = tk.Entry(self.frame, font=("Arial", 16), width=10)
        self.length_entry.grid(row=0, column=1, padx=5, pady=5)

        # Button to generate password
        self.generate_button = tk.Button(self.frame, text="Generate Password", command=self.generate_password, font=("Arial", 16), bg="#008080", fg="white", relief=tk.RAISED)
        self.generate_button.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

        # Label to display generated password
        self.password_label = tk.Label(self.frame, text="", font=("Arial", 16), bg="#f0f0f0")
        self.password_label.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

    def generate_password(self):
        try:
            length = int(self.length_entry.get())
            if length <= 0:
                raise ValueError("Length must be a positive integer")

            # Generate password
            password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=length))

            # Display generated password
            self.password_label.config(text="Generated Password: " + password)
        except ValueError as e:
            messagebox.showerror("Error", str(e))
        except Exception as e:
            messagebox.showerror("Error", "An unexpected error occurred")

def main():
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
