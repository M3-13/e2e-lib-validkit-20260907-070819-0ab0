def is_valid_isbn13(text: str) -> bool:
    if not isinstance(text, str):
        raise TypeError(f"is_valid_isbn13 expects str, got {type(text).__name__}")

    digits = text.replace("-", "").replace(" ", "")

    if len(digits) != 13 or not digits.isascii() or not digits.isdigit():
        return False

    total = sum(int(digit) * (1 if index % 2 == 0 else 3) for index, digit in enumerate(digits))
    return total % 10 == 0
