import random
import time
import tkinter as tk


class SimonGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Simon Game")
        self.sequence = []
        self.user_sequence = []
        self.buttons = {}
        self.colors = ["red", "green", "blue", "yellow"]
        self.create_widgets()
        self.start_game()

    def create_widgets(self):
        frame = tk.Frame(self.root)
        frame.pack()

        for color in self.colors:
            button = tk.Button(
                frame,
                bg=color,
                width=10,
                height=5,
                command=lambda c=color: self.user_click(c),
            )
            button.pack(side=tk.LEFT, padx=10, pady=10)
            self.buttons[color] = button

        self.start_button = tk.Button(self.root, text="Start", command=self.start_game)
        self.start_button.pack(pady=20)

        self.status_label = tk.Label(self.root, text="", font=("Helvetica", 14))
        self.status_label.pack(pady=10)

    def start_game(self):
        self.sequence = []
        self.user_sequence = []
        self.next_round()

    def next_round(self):
        self.user_sequence = []
        self.sequence.append(random.choice(self.colors))
        self.status_label.config(text=f"Round {len(self.sequence)}")
        self.play_sequence()

    def play_sequence(self):
        for i, color in enumerate(self.sequence):
            self.root.after(1000 * i, lambda c=color: self.flash_button(c))
        self.root.after(1000 * len(self.sequence), self.enable_buttons)

    def flash_button(self, color):
        button = self.buttons[color]
        original_color = button.cget("bg")
        button.config(bg="white")
        self.root.after(500, lambda: button.config(bg=original_color))

    def enable_buttons(self):
        for button in self.buttons.values():
            button.config(state=tk.NORMAL)

    def disable_buttons(self):
        for button in self.buttons.values():
            button.config(state=tk.DISABLED)

    def user_click(self, color):
        self.user_sequence.append(color)
        if self.user_sequence == self.sequence[: len(self.user_sequence)]:
            if len(self.user_sequence) == len(self.sequence):
                self.disable_buttons()
                self.root.after(1000, self.next_round)
        else:
            self.disable_buttons()
            self.status_label.config(text="Game Over! Click Start to play again.")
            self.start_button.config(state=tk.NORMAL)


if __name__ == "__main__":
    root = tk.Tk()
    game = SimonGame(root)
    root.mainloop()
