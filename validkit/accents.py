import unicodedata


def strip_accents(text: str) -> str:
    if not isinstance(text, str):
        raise TypeError("text must be a str")

    decomposed = unicodedata.normalize("NFD", text)
    return "".join(ch for ch in decomposed if unicodedata.category(ch) != "Mn")
