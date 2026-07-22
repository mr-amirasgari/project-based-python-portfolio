"""Core logic for checking happy numbers."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class HappyNumberResult:
    """Stores the result of a happy-number analysis."""

    number: int
    is_happy: bool
    sequence: tuple[int, ...]
    cycle: tuple[int, ...] = ()

    @property
    def iterations(self) -> int:
        """Number of transformations performed."""
        return max(0, len(self.sequence) - 1)


def sum_of_squared_digits(number: int) -> int:
    """Return the sum of the squares of the digits of ``number``."""
    return sum(int(digit) ** 2 for digit in str(number))


def analyze_happy_number(number: int) -> HappyNumberResult:
    """
    Analyze a positive integer and return its full transformation sequence.

    A happy number eventually reaches 1 after repeatedly replacing the number
    with the sum of the squares of its digits. An unhappy number enters a cycle.

    Args:
        number: Positive integer to analyze.

    Raises:
        TypeError: If ``number`` is not an integer.
        ValueError: If ``number`` is less than 1.
    """
    if isinstance(number, bool) or not isinstance(number, int):
        raise TypeError("number must be an integer")
    if number < 1:
        raise ValueError("number must be greater than zero")

    seen_index: dict[int, int] = {}
    sequence: list[int] = []
    current = number

    while current != 1 and current not in seen_index:
        seen_index[current] = len(sequence)
        sequence.append(current)
        current = sum_of_squared_digits(current)

    sequence.append(current)

    if current == 1:
        return HappyNumberResult(
            number=number,
            is_happy=True,
            sequence=tuple(sequence),
        )

    cycle_start = seen_index[current]
    return HappyNumberResult(
        number=number,
        is_happy=False,
        sequence=tuple(sequence),
        cycle=tuple(sequence[cycle_start:-1]),
    )


def is_happy(number: int) -> bool:
    """Return ``True`` if ``number`` is happy; otherwise return ``False``."""
    return analyze_happy_number(number).is_happy
