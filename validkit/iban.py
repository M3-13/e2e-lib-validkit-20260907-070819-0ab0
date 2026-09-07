def is_valid_iban(text: str) -> bool:
    if not isinstance(text, str):
        raise TypeError("text must be a str")

    compact = text.replace(" ", "")

    if any(not ch.isascii() or not ch.isalnum() for ch in compact):
        raise ValueError("text contains characters other than letters and digits")

    if not 15 <= len(compact) <= 34:
        return False

    rearranged = compact[4:] + compact[:4]
    digits = "".join(_char_to_digits(ch) for ch in rearranged)
    return int(digits) % 97 == 1


def _char_to_digits(ch: str) -> str:
    if "0" <= ch <= "9":
        return ch
    return str(10 + ord(ch.upper()) - ord("A"))
