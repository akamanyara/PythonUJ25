import tkinter as tk
import random


CHOICES = ["Rock", "Paper", "Scissors"]


def get_result(player, computer):
    if player == computer:
        return "Draw"
    if (
        (player == "Rock" and computer == "Scissors") or
        (player == "Paper" and computer == "Rock") or
        (player == "Scissors" and computer == "Paper")
    ):
        return "You win"
    return "You lose"


def play(player_choice):
    computer_choice = random.choice(CHOICES)
    result = get_result(player_choice, computer_choice)

    result_label.config(
        text=(
            f"Player: {player_choice}\n"
            f"Computer: {computer_choice}\n\n"
            f"Result: {result}"
        )
    )


# --- GUI setup ---

root = tk.Tk()
root.title("Rock Paper Scissors")
root.resizable(False, False)

title_label = tk.Label(root, text="Rock – Paper – Scissors", font=("Arial", 14))
title_label.pack(pady=10)

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

tk.Button(button_frame, text="Rock", width=10,
          command=lambda: play("Rock")).grid(row=0, column=0, padx=5)

tk.Button(button_frame, text="Paper", width=10,
          command=lambda: play("Paper")).grid(row=0, column=1, padx=5)

tk.Button(button_frame, text="Scissors", width=10,
          command=lambda: play("Scissors")).grid(row=0, column=2, padx=5)

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=15)

root.mainloop()