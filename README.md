<div align="center">

# Project-Based Python Portfolio

A growing collection of Python projects built, extended, and redesigned while studying project-based programming.

![Python](https://img.shields.io/badge/Python-3.12+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Projects](https://img.shields.io/badge/Projects-4%20of%2028-6C63FF?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-In%20Progress-F59E0B?style=for-the-badge)

</div>

---

## About

This repository contains a structured portfolio of Python projects.

The original project ideas are based on the
[Project-Based Python course by Pytopia](https://www.pytopia.ai/courses/project-based-python).

Each project is independently implemented, modified, documented, and improved to demonstrate my own learning and development process.

---

## Projects

| # | Project | Interface | Status |
|---|---|---|---|
| 01 | [Number Guesser](./projects/01-number-guesser) | CLI + PySide6 GUI | Completed |
| 02 | [Rock Paper Scissors](./projects/02-rock-paper-scissors-gui) | Tkinter GUI | Completed |
| 03 | [Password Generator](./projects/03-password-generator) | Tkinter GUI | Completed |
| 04 | [Password Generator — Streamlit](./projects/04-password-generator-streamlit) | Streamlit Web App | Completed |

More projects will be added progressively.

---

## Repository Structure

```text
project-based-python-portfolio/
├── projects/
│   ├── 01-number-guesser/
│   ├── 02-rock-paper-scissors-gui/
│   └── ...
├── .gitignore
└── README.md
```

Each project may contain:

```text
project-name/
├── README.md
├── main.py
├── src/
├── tests/
├── assets/
└── requirements.txt
```

The exact structure depends on the size and requirements of each project.

---

## Completed Projects

### 01. Number Guesser

A number-guessing game with two interfaces:

- Command-line interface
- Desktop graphical interface built with PySide6
- Input validation
- Hint generation
- Score tracking
- Restart and exit controls

[Open Number Guesser](./projects/01-number-guesser)

### 02. Rock Paper Scissors

A desktop Rock–Paper–Scissors game built with Python and Tkinter.

- Graphical Rock, Paper, and Scissors controls
- Random computer selection
- Player and computer score tracking
- Color-coded win, loss, and tie messages
- Reset button
- Object-oriented game logic

[Open Rock Paper Scissors](./projects/02-rock-paper-scissors-gui)


### 03. Password Generator

A desktop password generator built with Python, Tkinter, and NLTK.

- Numeric PIN generation
- Random passwords with optional numbers and symbols
- Memorable passwords using the NLTK words corpus
- Configurable length, separators, and capitalization
- Clipboard copy support
- Input validation and error handling

> This educational project uses Python's `random` module and is not intended for security-sensitive password generation.

[Open Password Generator](./projects/03-password-generator)

### 04. Password Generator — Streamlit

A web-based password generator built with Python, Streamlit, and NLTK.

- Random password generation
- Optional numbers and symbols
- Memorable word-based passwords
- Numeric PIN generation
- Interactive Streamlit interface
- Object-oriented generator classes

> This educational project uses Python's `random` module and is not intended for security-sensitive password generation.

[Open Streamlit Password Generator](./projects/04-password-generator-streamlit)
---

## Running a Project

Clone the repository:

```bash
git clone https://github.com/mr-amirasgari/project-based-python-portfolio.git
```

Enter the repository:

```bash
cd project-based-python-portfolio
```

Open the desired project folder:

```bash
cd projects/02-rock-paper-scissors-gui
```

Run the Rock Paper Scissors application:

```bash
python src/game.py
```

Each project includes its own README with project-specific setup and execution instructions.

---

## Goals

- Strengthen Python fundamentals
- Practice clean project structure
- Improve object-oriented programming skills
- Build command-line and graphical applications
- Add testing and documentation
- Refactor course exercises into original implementations
- Create a consistent public Python portfolio

---

## Progress

- [x] Create the portfolio repository
- [x] Add the first project
- [x] Add the second project
- [x] Add the third project
- [x] Add a repository-wide `.gitignore`
- [x] Standardize project organization
- [ ] Add automated tests
- [ ] Add continuous integration
- [ ] Complete all planned projects

---

## Attribution

The project ideas in this portfolio are inspired by the
[Project-Based Python course by Pytopia](https://www.pytopia.ai/courses/project-based-python).

The source code, project structure, added features, documentation, and redesigns in this repository represent my own learning work unless otherwise stated.

---

## Author

**Amir Mohammad Asgari**

[GitHub Profile](https://github.com/mr-amirasgari)

