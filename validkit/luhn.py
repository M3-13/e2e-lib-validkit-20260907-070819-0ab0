def luhn_check(digits: str) -> bool:
    if not isinstance(digits, str):
        raise TypeError(f"luhn_check expects str, got {type(digits).__name__}")

    if not digits:
        return False

    if not digits.isascii() or not digits.isdigit():
        raise ValueError("luhn_check expects a string containing only digits")

    total = 0
    for index, char in enumerate(reversed(digits)):
        value = int(char)
        if index % 2 == 1:
            value *= 2
            if value > 9:
                value -= 9
        total += value

    return total % 10 == 0
