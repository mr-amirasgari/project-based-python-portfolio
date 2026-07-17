def validate_number(value, start, end):
    value = value.strip()

    if value == "":
        return False, None, "Please enter a number."

    try:
        number = int(value)
    except ValueError:
        return False, None, "Please enter a valid integer."

    if number < start or number > end:
        return (
            False,
            None,
            f"Input must be between {start} and {end}."
        )

    return True, number, ""


def get_valid_input(start, end):
    while True:
        value = input(
            f"Enter a number between {start} and {end}: "
        )

        is_valid, number, error_message = validate_number(
            value,
            start,
            end
        )

        if is_valid:
            return number

        print(error_message)