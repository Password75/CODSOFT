import tkinter as tk
from tkinter import messagebox
import random

class RockPaperScissorsApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Rock Paper Scissors")
        self.master.configure(bg="#f0f0f0")
        self.user_score = 0
        self.computer_score = 0

        self.frame = tk.Frame(master, padx=50, pady=50, bg="#f0f0f0")
        self.frame.pack()

        self.instruction_label = tk.Label(self.frame, text="Choose Rock, Paper, or Scissors:", font=("Arial", 20), bg="#f0f0f0")
        self.instruction_label.grid(row=0, column=0, columnspan=3, padx=5, pady=5)

        self.rock_button = tk.Button(self.frame, text="Rock", command=lambda: self.play("Rock"), font=("Arial", 16), bg="#008080", fg="white", relief=tk.RAISED)
        self.rock_button.grid(row=1, column=0, padx=5, pady=5)
        self.paper_button = tk.Button(self.frame, text="Paper", command=lambda: self.play("Paper"), font=("Arial", 16), bg="#008080", fg="white", relief=tk.RAISED)
        self.paper_button.grid(row=1, column=1, padx=5, pady=5)
        self.scissors_button = tk.Button(self.frame, text="Scissors", command=lambda: self.play("Scissors"), font=("Arial", 16), bg="#008080", fg="white", relief=tk.RAISED)
        self.scissors_button.grid(row=1, column=2, padx=5, pady=5)

        self.result_label = tk.Label(self.frame, text="", font=("Arial", 20), bg="#f0f0f0")
        self.result_label.grid(row=2, column=0, columnspan=3, padx=5, pady=5)

        self.score_label = tk.Label(self.frame, text="User: 0   Computer: 0", font=("Arial", 16), bg="#f0f0f0")
        self.score_label.grid(row=3, column=0, columnspan=3, padx=5, pady=5)

        
        self.play_again_button = tk.Button(self.frame, text="Play Again", command=self.reset_game, font=("Arial", 16), bg="#008080", fg="white", relief=tk.RAISED)
        self.play_again_button.grid(row=4, column=0, columnspan=3, padx=5, pady=5)
        self.play_again_button.config(state=tk.DISABLED)

    def play(self, user_choice):
        choices = ["Rock", "Paper", "Scissors"]
        computer_choice = random.choice(choices)

        if user_choice == computer_choice:
            result = "It's a Tie!"
        elif (user_choice == "Rock" and computer_choice == "Scissors") or \
             (user_choice == "Paper" and computer_choice == "Rock") or \
             (user_choice == "Scissors" and computer_choice == "Paper"):
            result = "You Win!"
            self.user_score += 1
        else:
            result = "Computer Wins!"
            self.computer_score += 1

        self.result_label.config(text=f"Your Choice: {user_choice}\nComputer's Choice: {computer_choice}\n{result}")
        self.score_label.config(text=f"User: {self.user_score}   Computer: {self.computer_score}")
        self.play_again_button.config(state=tk.NORMAL)

    def reset_game(self):
        self.user_score = 0
        self.computer_score = 0
        self.result_label.config(text="")
        self.score_label.config(text="User: 0   Computer: 0")
        self.play_again_button.config(state=tk.DISABLED)

def main():
    root = tk.Tk()
    app = RockPaperScissorsApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
