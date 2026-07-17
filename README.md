<div align="center">

# Project-Based Python Portfolio

A growing collection of Python projects built, extended, and redesigned while studying project-based programming.

![Python](https://img.shields.io/badge/Python-3.12+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Projects](https://img.shields.io/badge/Projects-1%20of%2028-6C63FF?style=for-the-badge)
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
| 02 | Rock Paper Scissors | Planned | Upcoming |
| 03 | Password Generator | Planned | Upcoming |
| 04 | Coming soon | — | Upcoming |

More projects will be added progressively.

---

## Repository Structure

```text
project-based-python-portfolio/
├── projects/
│   ├── 01-number-guesser/
│   ├── 02-rock-paper-scissors/
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

## Current Project

### Number Guesser

A number-guessing game with two interfaces:

- Command-line interface
- Desktop graphical interface built with PySide6
- Input validation
- Hint generation
- Score tracking
- Restart and exit controls

[Open Number Guesser](./projects/01-number-guesser)

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

Open a project:

```bash
cd projects/01-number-guesser
```

Install its dependencies:

```bash
python -m pip install -r requirements.txt
```

Run the graphical version:

```bash
python main.py
```

Run the command-line version:

```bash
python cli.py
```

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