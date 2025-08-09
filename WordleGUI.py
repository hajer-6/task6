import tkinter as tk
from tkinter import messagebox
import random
from wordel import Wordle

COLOR_CORRECT = "#6aaa64"  
COLOR_PRESENT = "#c9b458"   
COLOR_ABSENT = "#050d11"    
COLOR_DEFAULT = "#d3d6da"   

def load_words(filename="words.txt"):
    with open(filename, "r") as file:
        words = [line.strip().lower() for line in file if len(line.strip()) == 5]
    return words

class WordleGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Wordle Game")
        self.game = Wordle(random.choice(load_words()))
        self.current_row = 0

        self.grid = [[None for _ in range(5)] for _ in range(6)]
        self.setup_grid()
        self.setup_input()

    def setup_grid(self):
        for row in range(6):
            for col in range(5):
                label = tk.Label(self.root, text=" ", width=4, height=2,
                                 font=('Helvetica', 24), bg=COLOR_DEFAULT, relief="solid", borderwidth=1)
                label.grid(row=row, column=col, padx=2, pady=2)
                self.grid[row][col] = label

    def setup_input(self):
        self.entry = tk.Entry(self.root, font=('Helvetica', 16))
        self.entry.grid(row=7, column=0, columnspan=3, padx=5, pady=10)
        self.entry.focus()

        button = tk.Button(self.root, text="Submit", font=('Helvetica', 16), command=self.submit_guess)
        button.grid(row=7, column=3, columnspan=2, padx=5, pady=10)

    def submit_guess(self):
        guess = self.entry.get().lower()

        if len(guess) != 5 or guess not in load_words():
            messagebox.showerror("Invalid", "Enter a valid 5-letter word from the list.")
            return

        feedback = self.game.check_guess(guess)

        for col in range(5):
            letter = guess[col].upper()
            label = self.grid[self.current_row][col]
            label.config(text=letter)

            color = {
                "green": COLOR_CORRECT,
                "yellow": COLOR_PRESENT,
                "gray": COLOR_ABSENT
            }.get(feedback[col], COLOR_DEFAULT)

            label.config(bg=color, fg="white")

        self.current_row += 1
        self.entry.delete(0, tk.END)

        if self.game.win(guess):
            messagebox.showinfo(" Correct!", "You guessed the word!")
            self.entry.config(state='disabled')
        elif self.game.is_game_over():
            messagebox.showinfo(" Game Over", f"The word was: {self.game.secret.upper()}")
            self.entry.config(state='disabled')

if __name__ == "__main__":
    root = tk.Tk()
    app = WordleGUI(root)
    root.mainloop()