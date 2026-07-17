from PySide6.QtCore import Qt
from PySide6.QtGui import QIntValidator
from PySide6.QtWidgets import (
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMainWindow,
    QMessageBox,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

from src.game_logic.hint_generator import provide_hint
from src.game_logic.number_generator import generate_random_number
from src.game_logic.scorer import Score
from src.utils.input_validator import validate_number


class MainWindow(QMainWindow):
    MINIMUM_NUMBER = 1
    MAXIMUM_NUMBER = 100

    def __init__(self):
        super().__init__()

        self.score = Score()

        self.actual_number = generate_random_number(
            self.MINIMUM_NUMBER,
            self.MAXIMUM_NUMBER
        )

        self.setWindowTitle("Number Guesser Game")
        self.setFixedSize(500, 440)

        self.create_user_interface()
        self.apply_styles()

    def create_user_interface(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QVBoxLayout(central_widget)
        main_layout.setContentsMargins(40, 35, 40, 35)
        main_layout.setSpacing(16)

        title_label = QLabel("Number Guesser")
        title_label.setObjectName("titleLabel")
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        description_label = QLabel(
            "Guess a number between 1 and 100"
        )
        description_label.setObjectName("descriptionLabel")
        description_label.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        self.score_label = QLabel()
        self.score_label.setObjectName("scoreLabel")
        self.score_label.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        self.guess_input = QLineEdit()
        self.guess_input.setObjectName("guessInput")
        self.guess_input.setPlaceholderText(
            "Enter your guess"
        )
        self.guess_input.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )
        self.guess_input.setMaxLength(3)

        number_validator = QIntValidator(
            self.MINIMUM_NUMBER,
            self.MAXIMUM_NUMBER,
            self
        )
        self.guess_input.setValidator(number_validator)

        self.check_button = QPushButton("Check Guess")
        self.check_button.setObjectName("checkButton")

        self.message_label = QLabel(
            "Enter your first guess."
        )
        self.message_label.setObjectName("messageLabel")
        self.message_label.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )
        self.message_label.setWordWrap(True)

        bottom_button_layout = QHBoxLayout()
        bottom_button_layout.setSpacing(12)

        self.new_game_button = QPushButton("New Game")
        self.new_game_button.setObjectName("secondaryButton")

        self.exit_button = QPushButton("Exit")
        self.exit_button.setObjectName("secondaryButton")

        bottom_button_layout.addWidget(
            self.new_game_button
        )
        bottom_button_layout.addWidget(
            self.exit_button
        )

        main_layout.addWidget(title_label)
        main_layout.addWidget(description_label)
        main_layout.addSpacing(5)
        main_layout.addWidget(self.score_label)
        main_layout.addSpacing(5)
        main_layout.addWidget(self.guess_input)
        main_layout.addWidget(self.check_button)
        main_layout.addWidget(self.message_label)
        main_layout.addStretch()
        main_layout.addLayout(bottom_button_layout)

        self.check_button.clicked.connect(
            self.check_guess
        )

        self.new_game_button.clicked.connect(
            self.reset_game
        )

        self.exit_button.clicked.connect(
            self.close
        )

        self.guess_input.returnPressed.connect(
            self.check_guess
        )

        self.update_score_label()
        self.guess_input.setFocus()

    def check_guess(self):
        is_valid, user_guess, error_message = (
            validate_number(
                self.guess_input.text(),
                self.MINIMUM_NUMBER,
                self.MAXIMUM_NUMBER
            )
        )

        if not is_valid:
            self.show_message(
                error_message,
                message_type="error"
            )
            self.guess_input.setFocus()
            return

        if user_guess == self.actual_number:
            self.handle_correct_guess()
            return

        hint = provide_hint(
            user_guess,
            self.actual_number
        )

        self.show_message(
            hint,
            message_type="hint"
        )

        self.score.decrease()
        self.update_score_label()

        self.guess_input.clear()
        self.guess_input.setFocus()

    def handle_correct_guess(self):
        final_score = self.score.get_score()

        self.show_message(
            (
                "Congratulations! "
                f"Your final score is {final_score}."
            ),
            message_type="success"
        )

        answer = QMessageBox.question(
            self,
            "Congratulations",
            (
                "You guessed the correct number!\n\n"
                f"Final score: {final_score}\n\n"
                "Do you want to play again?"
            ),
            (
                QMessageBox.StandardButton.Yes
                | QMessageBox.StandardButton.No
            )
        )

        if answer == QMessageBox.StandardButton.Yes:
            self.reset_game()
        else:
            self.close()

    def reset_game(self):
        self.actual_number = generate_random_number(
            self.MINIMUM_NUMBER,
            self.MAXIMUM_NUMBER
        )

        self.score.reset()
        self.update_score_label()

        self.guess_input.clear()

        self.show_message(
            "A new number has been generated.",
            message_type="normal"
        )

        self.guess_input.setFocus()

    def update_score_label(self):
        current_score = self.score.get_score()

        self.score_label.setText(
            f"Score: {current_score}"
        )

    def show_message(
        self,
        message,
        message_type="normal"
    ):
        message_colors = {
            "normal": "#cbd5e1",
            "error": "#f87171",
            "hint": "#facc15",
            "success": "#4ade80"
        }

        color = message_colors.get(
            message_type,
            message_colors["normal"]
        )

        self.message_label.setText(message)

        self.message_label.setStyleSheet(
            f"""
            color: {color};
            font-size: 14px;
            font-weight: bold;
            """
        )

    def apply_styles(self):
        self.setStyleSheet(
            """
            QMainWindow {
                background-color: #111827;
            }

            QLabel {
                color: #f9fafb;
                font-family: Arial;
            }

            QLabel#titleLabel {
                font-size: 30px;
                font-weight: bold;
            }

            QLabel#descriptionLabel {
                color: #cbd5e1;
                font-size: 15px;
            }

            QLabel#scoreLabel {
                padding: 12px;
                background-color: #1f2937;
                border: 1px solid #374151;
                border-radius: 15px;
                color: #a78bfa;
                font-size: 20px;
                font-weight: bold;
            }

            QLabel#messageLabel {
                min-height: 55px;
                font-size: 14px;
            }

            QLineEdit#guessInput {
                padding: 14px;
                background-color: #1f2937;
                border: 2px solid #374151;
                border-radius: 12px;
                color: #ffffff;
                font-size: 19px;
            }

            QLineEdit#guessInput:focus {
                border: 2px solid #8b5cf6;
            }

            QPushButton {
                min-height: 24px;
                padding: 12px;
                border: none;
                border-radius: 10px;
                color: #ffffff;
                font-size: 14px;
                font-weight: bold;
            }

            QPushButton#checkButton {
                background-color: #7c3aed;
            }

            QPushButton#checkButton:hover {
                background-color: #8b5cf6;
            }

            QPushButton#checkButton:pressed {
                background-color: #6d28d9;
            }

            QPushButton#secondaryButton {
                background-color: #374151;
            }

            QPushButton#secondaryButton:hover {
                background-color: #4b5563;
            }

            QPushButton#secondaryButton:pressed {
                background-color: #1f2937;
            }
            """
        )
