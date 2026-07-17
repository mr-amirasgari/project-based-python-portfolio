def provide_hint(guess, actual_number):
    if guess < actual_number:
        return "Your guess is too low. Try a higher number."

    if guess > actual_number:
        return "Your guess is too high. Try a lower number."

    return "Correct!"