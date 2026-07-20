import random
import string
import tkinter as tk
from abc import ABC, abstractmethod
from tkinter import messagebox, ttk

import nltk


class PasswordGenerator(ABC):
    """Base class for all password generators."""

    @abstractmethod
    def generate(self) -> str:
        pass


class PinGenerator(PasswordGenerator):
    """Generate a numeric PIN."""

    def __init__(self, length: int = 4):
        if length < 1:
            raise ValueError("PIN length must be at least 1.")

        self.length = length

    def generate(self) -> str:
        return "".join(
            random.choice(string.digits)
            for _ in range(self.length)
        )


class RandomPasswordGenerator(PasswordGenerator):
    """Generate a password using letters, numbers, and symbols."""

    def __init__(
        self,
        length: int = 8,
        include_numbers: bool = False,
        include_symbols: bool = False,
    ):
        if length < 1:
            raise ValueError("Password length must be at least 1.")

        self.length = length
        self.include_numbers = include_numbers
        self.include_symbols = include_symbols

        self.characters = string.ascii_letters

        if self.include_numbers:
            self.characters += string.digits

        if self.include_symbols:
            self.characters += string.punctuation

    def generate(self) -> str:
        password_characters = []

        # Ensure at least one number is included.
        if self.include_numbers:
            password_characters.append(
                random.choice(string.digits)
            )

        # Ensure at least one symbol is included.
        if self.include_symbols:
            password_characters.append(
                random.choice(string.punctuation)
            )

        if self.length < len(password_characters):
            raise ValueError(
                "Password length is too short "
                "for the selected options."
            )

        remaining_length = (
            self.length - len(password_characters)
        )

        password_characters.extend(
            random.choice(self.characters)
            for _ in range(remaining_length)
        )

        random.shuffle(password_characters)

        return "".join(password_characters)


class MemoryPasswordGenerator(PasswordGenerator):
    """Generate a memorable password using NLTK words."""

    def __init__(
        self,
        num_words: int = 4,
        separator: str = "-",
        capitalize: bool = False,
        vocabulary: list[str] | None = None,
    ):
        if num_words < 1:
            raise ValueError(
                "Number of words must be at least 1."
            )

        if vocabulary is None:
            vocabulary = self.load_nltk_words()

        cleaned_vocabulary = [
            word.lower()
            for word in vocabulary
            if word.isalpha() and 4 <= len(word) <= 10
        ]

        if not cleaned_vocabulary:
            raise ValueError(
                "The vocabulary does not contain valid words."
            )

        self.num_words = num_words
        self.capitalize = capitalize
        self.separator = separator
        self.vocabulary = cleaned_vocabulary

    @staticmethod
    def load_nltk_words() -> list[str]:
        """Load NLTK words and download them if needed."""

        try:
            from nltk.corpus import words

            return words.words()

        except LookupError:
            downloaded = nltk.download(
                "words",
                quiet=True,
            )

            if not downloaded:
                raise RuntimeError(
                    "NLTK words corpus could not be downloaded. "
                    "Check your internet connection."
                )

            from nltk.corpus import words

            return words.words()

    def generate(self) -> str:
        selected_words = [
            random.choice(self.vocabulary)
            for _ in range(self.num_words)
        ]

        if self.capitalize:
            selected_words = [
                word.capitalize()
                if random.choice([True, False])
                else word.lower()
                for word in selected_words
            ]

        return self.separator.join(selected_words)


class PasswordGeneratorApp(tk.Tk):
    """Graphical interface for the password generator."""

    def __init__(self):
        super().__init__()

        self.title("Password Generator")
        self.geometry("620x530")
        self.minsize(600, 500)

        self.configure(
            padx=22,
            pady=18,
        )

        self.generated_password = tk.StringVar()

        self.status_text = tk.StringVar(
            value="Select a generator and click Generate."
        )

        self.create_styles()
        self.create_widgets()

    def create_styles(self):
        style = ttk.Style(self)

        try:
            style.theme_use("clam")
        except tk.TclError:
            pass

        style.configure(
            "Title.TLabel",
            font=("Segoe UI", 20, "bold"),
        )

        style.configure(
            "Subtitle.TLabel",
            font=("Segoe UI", 10),
        )

        style.configure(
            "Result.TEntry",
            font=("Consolas", 14),
            padding=8,
        )

        style.configure(
            "Generate.TButton",
            font=("Segoe UI", 11, "bold"),
            padding=9,
        )

    def create_widgets(self):
        title = ttk.Label(
            self,
            text="Password Generator",
            style="Title.TLabel",
        )
        title.pack(anchor="w")

        subtitle = ttk.Label(
            self,
            text=(
                "Generate a PIN, a random password, "
                "or a memorable NLTK password."
            ),
            style="Subtitle.TLabel",
        )
        subtitle.pack(
            anchor="w",
            pady=(2, 18),
        )

        self.notebook = ttk.Notebook(self)
        self.notebook.pack(
            fill="both",
            expand=True,
        )

        self.pin_tab = ttk.Frame(
            self.notebook,
            padding=20,
        )

        self.random_tab = ttk.Frame(
            self.notebook,
            padding=20,
        )

        self.memory_tab = ttk.Frame(
            self.notebook,
            padding=20,
        )

        self.notebook.add(
            self.pin_tab,
            text="PIN",
        )

        self.notebook.add(
            self.random_tab,
            text="Random Password",
        )

        self.notebook.add(
            self.memory_tab,
            text="Memorable Password",
        )

        self.create_pin_tab()
        self.create_random_tab()
        self.create_memory_tab()

        result_frame = ttk.LabelFrame(
            self,
            text="Generated Result",
            padding=12,
        )

        result_frame.pack(
            fill="x",
            pady=(16, 8),
        )

        result_entry = ttk.Entry(
            result_frame,
            textvariable=self.generated_password,
            state="readonly",
            style="Result.TEntry",
        )

        result_entry.pack(
            side="left",
            fill="x",
            expand=True,
            padx=(0, 8),
        )

        copy_button = ttk.Button(
            result_frame,
            text="Copy",
            command=self.copy_password,
        )

        copy_button.pack(side="right")

        generate_button = ttk.Button(
            self,
            text="Generate Password",
            command=self.generate_password,
            style="Generate.TButton",
        )

        generate_button.pack(
            fill="x",
            pady=(2, 8),
        )

        status_label = ttk.Label(
            self,
            textvariable=self.status_text,
        )

        status_label.pack(anchor="w")

    def create_pin_tab(self):
        ttk.Label(
            self.pin_tab,
            text="PIN length:",
        ).grid(
            row=0,
            column=0,
            sticky="w",
            pady=8,
        )

        self.pin_length = tk.IntVar(value=4)

        ttk.Spinbox(
            self.pin_tab,
            from_=1,
            to=20,
            textvariable=self.pin_length,
            width=10,
        ).grid(
            row=0,
            column=1,
            sticky="w",
            padx=12,
            pady=8,
        )

        ttk.Label(
            self.pin_tab,
            text="Example: 4827",
        ).grid(
            row=1,
            column=0,
            columnspan=2,
            sticky="w",
            pady=(8, 0),
        )

    def create_random_tab(self):
        ttk.Label(
            self.random_tab,
            text="Password length:",
        ).grid(
            row=0,
            column=0,
            sticky="w",
            pady=8,
        )

        self.random_length = tk.IntVar(value=12)

        ttk.Spinbox(
            self.random_tab,
            from_=1,
            to=100,
            textvariable=self.random_length,
            width=10,
        ).grid(
            row=0,
            column=1,
            sticky="w",
            padx=12,
            pady=8,
        )

        self.include_numbers = tk.BooleanVar(
            value=True
        )

        self.include_symbols = tk.BooleanVar(
            value=True
        )

        ttk.Checkbutton(
            self.random_tab,
            text="Include numbers",
            variable=self.include_numbers,
        ).grid(
            row=1,
            column=0,
            columnspan=2,
            sticky="w",
            pady=8,
        )

        ttk.Checkbutton(
            self.random_tab,
            text="Include symbols",
            variable=self.include_symbols,
        ).grid(
            row=2,
            column=0,
            columnspan=2,
            sticky="w",
            pady=8,
        )

    def create_memory_tab(self):
        ttk.Label(
            self.memory_tab,
            text="Number of words:",
        ).grid(
            row=0,
            column=0,
            sticky="w",
            pady=8,
        )

        self.num_words = tk.IntVar(value=4)

        ttk.Spinbox(
            self.memory_tab,
            from_=1,
            to=12,
            textvariable=self.num_words,
            width=10,
        ).grid(
            row=0,
            column=1,
            sticky="w",
            padx=12,
            pady=8,
        )

        ttk.Label(
            self.memory_tab,
            text="Separator:",
        ).grid(
            row=1,
            column=0,
            sticky="w",
            pady=8,
        )

        self.separator = tk.StringVar(
            value="-"
        )

        separator_box = ttk.Combobox(
            self.memory_tab,
            textvariable=self.separator,
            values=("-", "_", ".", " ", "@"),
            width=8,
        )

        separator_box.grid(
            row=1,
            column=1,
            sticky="w",
            padx=12,
            pady=8,
        )

        self.capitalize_words = tk.BooleanVar(
            value=True
        )

        ttk.Checkbutton(
            self.memory_tab,
            text="Randomly capitalize words",
            variable=self.capitalize_words,
        ).grid(
            row=2,
            column=0,
            columnspan=2,
            sticky="w",
            pady=8,
        )

        ttk.Label(
            self.memory_tab,
            text=(
                "The NLTK words corpus is downloaded "
                "automatically the first time."
            ),
            wraplength=470,
        ).grid(
            row=3,
            column=0,
            columnspan=2,
            sticky="w",
            pady=(12, 0),
        )

    def generate_password(self):
        try:
            selected_tab = self.notebook.index(
                self.notebook.select()
            )

            if selected_tab == 0:
                generator = PinGenerator(
                    length=self.pin_length.get()
                )

            elif selected_tab == 1:
                generator = RandomPasswordGenerator(
                    length=self.random_length.get(),
                    include_numbers=(
                        self.include_numbers.get()
                    ),
                    include_symbols=(
                        self.include_symbols.get()
                    ),
                )

            else:
                self.status_text.set(
                    "Loading the NLTK vocabulary..."
                )

                self.update_idletasks()

                generator = MemoryPasswordGenerator(
                    num_words=self.num_words.get(),
                    separator=self.separator.get(),
                    capitalize=(
                        self.capitalize_words.get()
                    ),
                )

            password = generator.generate()

            self.generated_password.set(password)

            self.status_text.set(
                f"Generated successfully. "
                f"Length: {len(password)}"
            )

        except (ValueError, tk.TclError) as error:
            messagebox.showerror(
                "Invalid Input",
                str(error),
            )

            self.status_text.set(
                "Please check the entered values."
            )

        except Exception as error:
            messagebox.showerror(
                "Generation Error",
                str(error),
            )

            self.status_text.set(
                "Password generation failed."
            )

    def copy_password(self):
        password = self.generated_password.get()

        if not password:
            messagebox.showwarning(
                "Nothing to Copy",
                "Generate a password first.",
            )
            return

        self.clipboard_clear()
        self.clipboard_append(password)
        self.update()

        self.status_text.set(
            "Password copied to the clipboard."
        )


if __name__ == "__main__":
    app = PasswordGeneratorApp()
    app.mainloop()