import random
import tkinter as tk
from tkinter import messagebox


class RockPaperScissors:
    """Handles the game logic and score management."""

    def __init__(self, name):
        """Initialize player information, choices, and scores."""
        self.choices = ["rock", "paper", "scissors"]
        self.player_name = name
        self.player_score = 0
        self.computer_score = 0

    def get_computer_choice(self):
        """Return a random choice for the computer."""
        return random.choice(self.choices)

    def decide_winner(self, user_choice, computer_choice):
        """
        Determine the winner of a round.

        Returns:
            tuple: Winner type and result message.
        """
        if user_choice == computer_choice:
            return "tie", f"Both selected {user_choice}. It's a tie!"

        winning_combinations = [
            ("rock", "scissors"),
            ("scissors", "paper"),
            ("paper", "rock")
        ]

        if (user_choice, computer_choice) in winning_combinations:
            self.player_score += 1

            return (
                "player",
                f"{self.player_name} wins! "
                f"{user_choice.capitalize()} beats "
                f"{computer_choice.capitalize()}."
            )

        self.computer_score += 1

        return (
            "computer",
            f"Computer wins! "
            f"{computer_choice.capitalize()} beats "
            f"{user_choice.capitalize()}."
        )

    def reset_scores(self):
        """Reset player and computer scores."""
        self.player_score = 0
        self.computer_score = 0


class GameUI:
    """Creates and manages the Tkinter user interface."""

    def __init__(self, root):
        """Configure the main window and create interface widgets."""
        self.root = root
        self.root.title("Rock Paper Scissors")
        self.root.geometry("600x520")
        self.root.resizable(False, False)
        self.root.configure(bg="#1e293b")

        self.game = RockPaperScissors("Player")

        self.create_widgets()

    def create_widgets(self):
        """Create labels, buttons, and the scoreboard."""

        title_label = tk.Label(
            self.root,
            text="Rock Paper Scissors",
            font=("Arial", 26, "bold"),
            bg="#1e293b",
            fg="white"
        )
        title_label.pack(pady=(25, 10))

        subtitle_label = tk.Label(
            self.root,
            text="Choose one of the options",
            font=("Arial", 13),
            bg="#1e293b",
            fg="#cbd5e1"
        )
        subtitle_label.pack(pady=(0, 25))

        # Frame containing the game choice buttons
        buttons_frame = tk.Frame(
            self.root,
            bg="#1e293b"
        )
        buttons_frame.pack()

        rock_button = tk.Button(
            buttons_frame,
            text="🪨\nRock",
            font=("Arial", 16, "bold"),
            width=9,
            height=4,
            bg="#475569",
            fg="white",
            activebackground="#64748b",
            activeforeground="white",
            cursor="hand2",
            command=lambda: self.play_round("rock")
        )
        rock_button.grid(row=0, column=0, padx=8)

        paper_button = tk.Button(
            buttons_frame,
            text="📄\nPaper",
            font=("Arial", 16, "bold"),
            width=9,
            height=4,
            bg="#2563eb",
            fg="white",
            activebackground="#3b82f6",
            activeforeground="white",
            cursor="hand2",
            command=lambda: self.play_round("paper")
        )
        paper_button.grid(row=0, column=1, padx=8)

        scissors_button = tk.Button(
            buttons_frame,
            text="✂\nScissors",
            font=("Arial", 16, "bold"),
            width=9,
            height=4,
            bg="#dc2626",
            fg="white",
            activebackground="#ef4444",
            activeforeground="white",
            cursor="hand2",
            command=lambda: self.play_round("scissors")
        )
        scissors_button.grid(row=0, column=2, padx=8)

        self.choices_label = tk.Label(
            self.root,
            text="Player: -\nComputer: -",
            font=("Arial", 14),
            bg="#1e293b",
            fg="#e2e8f0",
            justify="center"
        )
        self.choices_label.pack(pady=25)

        self.result_label = tk.Label(
            self.root,
            text="The result will appear here.",
            font=("Arial", 15, "bold"),
            bg="#1e293b",
            fg="#facc15",
            wraplength=520,
            justify="center"
        )
        self.result_label.pack(pady=(0, 20))

        self.score_label = tk.Label(
            self.root,
            text="Player: 0   |   Computer: 0",
            font=("Arial", 16, "bold"),
            bg="#0f172a",
            fg="white",
            width=40,
            pady=10
        )
        self.score_label.pack(pady=10)

        reset_button = tk.Button(
            self.root,
            text="Reset Game",
            font=("Arial", 12, "bold"),
            bg="#f59e0b",
            fg="#1e293b",
            activebackground="#fbbf24",
            cursor="hand2",
            width=15,
            command=self.reset_game
        )
        reset_button.pack(pady=10)

    def play_round(self, player_choice):
        """Play one round and display the result."""
        computer_choice = self.game.get_computer_choice()

        winner, message = self.game.decide_winner(
            player_choice,
            computer_choice
        )

        self.choices_label.config(
            text=(
                f"Player: {player_choice.capitalize()}\n"
                f"Computer: {computer_choice.capitalize()}"
            )
        )

        self.result_label.config(text=message)

        # Change result color based on the winner
        if winner == "player":
            self.result_label.config(fg="#4ade80")
        elif winner == "computer":
            self.result_label.config(fg="#f87171")
        else:
            self.result_label.config(fg="#facc15")

        self.update_score()

    def update_score(self):
        """Update the scoreboard label."""
        self.score_label.config(
            text=(
                f"Player: {self.game.player_score}"
                f"   |   "
                f"Computer: {self.game.computer_score}"
            )
        )

    def reset_game(self):
        """Reset scores and restore the initial interface state."""
        self.game.reset_scores()

        self.choices_label.config(
            text="Player: -\nComputer: -"
        )

        self.result_label.config(
            text="The result will appear here.",
            fg="#facc15"
        )

        self.update_score()

        messagebox.showinfo(
            "Reset",
            "The game scores have been reset."
        )


def main():
    """Start the application."""
    root = tk.Tk()
    GameUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()