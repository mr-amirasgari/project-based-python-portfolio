"""Tkinter GUI for the Happy Number Checker."""

from __future__ import annotations

import tkinter as tk
from tkinter import messagebox, ttk

from .core import HappyNumberResult, analyze_happy_number, sum_of_squared_digits


class HappyNumberApp(tk.Tk):
    """Desktop application for analyzing happy numbers."""

    BG = "#f4f6fb"
    CARD = "#ffffff"
    TEXT = "#172033"
    MUTED = "#667085"
    ACCENT = "#4f46e5"
    SUCCESS = "#15803d"
    DANGER = "#b42318"

    def __init__(self) -> None:
        super().__init__()
        self.title("Happy Number Checker")
        self.geometry("780x620")
        self.minsize(680, 520)
        self.configure(bg=self.BG)

        self.number_var = tk.StringVar()
        self.status_var = tk.StringVar(value="Enter a positive integer.")
        self.summary_var = tk.StringVar(value="No number analyzed yet.")

        self._configure_styles()
        self._build_ui()
        self.bind("<Return>", lambda _event: self.check_number())
        self.after(100, self.number_entry.focus_set)

    def _configure_styles(self) -> None:
        style = ttk.Style(self)
        style.theme_use("clam")

        style.configure(
            "Primary.TButton",
            font=("Segoe UI", 11, "bold"),
            padding=(18, 10),
            background=self.ACCENT,
            foreground="white",
            borderwidth=0,
        )
        style.map(
            "Primary.TButton",
            background=[("active", "#4338ca"), ("pressed", "#3730a3")],
        )

        style.configure(
            "Secondary.TButton",
            font=("Segoe UI", 10),
            padding=(14, 9),
            background="#e9ecf5",
            foreground=self.TEXT,
            borderwidth=0,
        )
        style.map("Secondary.TButton", background=[("active", "#dfe3ee")])

        style.configure(
            "Steps.Treeview",
            font=("Segoe UI", 10),
            rowheight=30,
            background=self.CARD,
            fieldbackground=self.CARD,
            foreground=self.TEXT,
            borderwidth=0,
        )
        style.configure(
            "Steps.Treeview.Heading",
            font=("Segoe UI", 10, "bold"),
            background="#eef1f7",
            foreground=self.TEXT,
            relief="flat",
        )
        style.map("Steps.Treeview.Heading", background=[("active", "#e5e8f0")])

    def _build_ui(self) -> None:
        container = tk.Frame(self, bg=self.BG)
        container.pack(fill="both", expand=True, padx=28, pady=24)

        tk.Label(
            container,
            text="Happy Number Checker",
            font=("Segoe UI", 24, "bold"),
            bg=self.BG,
            fg=self.TEXT,
        ).pack(anchor="w")

        tk.Label(
            container,
            text="Check whether a number reaches 1 or falls into a repeating cycle.",
            font=("Segoe UI", 11),
            bg=self.BG,
            fg=self.MUTED,
        ).pack(anchor="w", pady=(4, 18))

        input_card = tk.Frame(
            container,
            bg=self.CARD,
            highlightthickness=1,
            highlightbackground="#e4e7ec",
        )
        input_card.pack(fill="x")

        tk.Label(
            input_card,
            text="Positive integer",
            font=("Segoe UI", 10, "bold"),
            bg=self.CARD,
            fg=self.TEXT,
        ).pack(anchor="w", padx=20, pady=(18, 7))

        input_row = tk.Frame(input_card, bg=self.CARD)
        input_row.pack(fill="x", padx=20, pady=(0, 18))

        self.number_entry = tk.Entry(
            input_row,
            textvariable=self.number_var,
            font=("Segoe UI", 15),
            bg="#f9fafb",
            fg=self.TEXT,
            insertbackground=self.TEXT,
            relief="flat",
            highlightthickness=1,
            highlightbackground="#d0d5dd",
            highlightcolor=self.ACCENT,
        )
        self.number_entry.pack(side="left", fill="x", expand=True, ipady=10)

        ttk.Button(
            input_row,
            text="Analyze",
            style="Primary.TButton",
            command=self.check_number,
        ).pack(side="left", padx=(12, 0))

        ttk.Button(
            input_row,
            text="Clear",
            style="Secondary.TButton",
            command=self.clear_all,
        ).pack(side="left", padx=(8, 0))

        result_card = tk.Frame(
            container,
            bg=self.CARD,
            highlightthickness=1,
            highlightbackground="#e4e7ec",
        )
        result_card.pack(fill="x", pady=(16, 16))

        result_top = tk.Frame(result_card, bg=self.CARD)
        result_top.pack(fill="x", padx=20, pady=(17, 8))

        self.result_badge = tk.Label(
            result_top,
            text="WAITING",
            font=("Segoe UI", 9, "bold"),
            bg="#eef1f7",
            fg=self.MUTED,
            padx=10,
            pady=5,
        )
        self.result_badge.pack(side="left")

        tk.Label(
            result_top,
            textvariable=self.summary_var,
            font=("Segoe UI", 15, "bold"),
            bg=self.CARD,
            fg=self.TEXT,
        ).pack(side="left", padx=(12, 0))

        tk.Label(
            result_card,
            textvariable=self.status_var,
            font=("Segoe UI", 10),
            bg=self.CARD,
            fg=self.MUTED,
            wraplength=690,
            justify="left",
        ).pack(anchor="w", padx=20, pady=(0, 17))

        table_card = tk.Frame(
            container,
            bg=self.CARD,
            highlightthickness=1,
            highlightbackground="#e4e7ec",
        )
        table_card.pack(fill="both", expand=True)

        table_header = tk.Frame(table_card, bg=self.CARD)
        table_header.pack(fill="x", padx=18, pady=(14, 8))

        tk.Label(
            table_header,
            text="Calculation steps",
            font=("Segoe UI", 12, "bold"),
            bg=self.CARD,
            fg=self.TEXT,
        ).pack(side="left")

        tk.Label(
            table_header,
            text="n → sum of squared digits",
            font=("Segoe UI", 9),
            bg=self.CARD,
            fg=self.MUTED,
        ).pack(side="right")

        table_frame = tk.Frame(table_card, bg=self.CARD)
        table_frame.pack(fill="both", expand=True, padx=18, pady=(0, 18))

        self.steps_tree = ttk.Treeview(
            table_frame,
            columns=("step", "number", "calculation", "result"),
            show="headings",
            style="Steps.Treeview",
        )
        self.steps_tree.heading("step", text="Step")
        self.steps_tree.heading("number", text="Current number")
        self.steps_tree.heading("calculation", text="Calculation")
        self.steps_tree.heading("result", text="Next value")

        self.steps_tree.column("step", width=70, anchor="center", stretch=False)
        self.steps_tree.column("number", width=130, anchor="center")
        self.steps_tree.column("calculation", width=290, anchor="w")
        self.steps_tree.column("result", width=110, anchor="center")

        scrollbar = ttk.Scrollbar(
            table_frame,
            orient="vertical",
            command=self.steps_tree.yview,
        )
        self.steps_tree.configure(yscrollcommand=scrollbar.set)

        self.steps_tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

    def _parse_input(self) -> int:
        raw_value = self.number_var.get().strip()
        if not raw_value:
            raise ValueError("Please enter a number.")
        if not raw_value.isdigit():
            raise ValueError("Only positive whole numbers are accepted.")

        number = int(raw_value)
        if number < 1:
            raise ValueError("The number must be greater than zero.")
        return number

    @staticmethod
    def _calculation_text(number: int) -> str:
        digits = list(str(number))
        return " + ".join(f"{digit}²" for digit in digits)

    def check_number(self) -> None:
        try:
            number = self._parse_input()
            result = analyze_happy_number(number)
        except ValueError as exc:
            messagebox.showwarning("Invalid input", str(exc), parent=self)
            self.number_entry.focus_set()
            return

        self._render_result(result)

    def _render_result(self, result: HappyNumberResult) -> None:
        self._clear_steps()

        for index, current in enumerate(result.sequence[:-1], start=1):
            next_value = sum_of_squared_digits(current)
            self.steps_tree.insert(
                "",
                "end",
                values=(
                    index,
                    current,
                    self._calculation_text(current),
                    next_value,
                ),
            )

        if result.is_happy:
            self.result_badge.configure(
                text="HAPPY",
                bg="#dcfce7",
                fg=self.SUCCESS,
            )
            self.summary_var.set(f"{result.number} is a happy number")
            self.status_var.set(
                f"It reached 1 after {result.iterations} transformation(s). "
                f"Sequence: {' → '.join(map(str, result.sequence))}"
            )
        else:
            self.result_badge.configure(
                text="NOT HAPPY",
                bg="#fee4e2",
                fg=self.DANGER,
            )
            self.summary_var.set(f"{result.number} is not a happy number")
            cycle_text = " → ".join(map(str, result.cycle))
            self.status_var.set(
                f"It entered a repeating cycle after {result.iterations} "
                f"transformation(s). Cycle: {cycle_text} → {result.cycle[0]}"
            )

    def _clear_steps(self) -> None:
        for item in self.steps_tree.get_children():
            self.steps_tree.delete(item)

    def clear_all(self) -> None:
        self.number_var.set("")
        self._clear_steps()
        self.result_badge.configure(
            text="WAITING",
            bg="#eef1f7",
            fg=self.MUTED,
        )
        self.summary_var.set("No number analyzed yet.")
        self.status_var.set("Enter a positive integer.")
        self.number_entry.focus_set()


def run() -> None:
    """Run the desktop application."""
    app = HappyNumberApp()
    app.mainloop()
