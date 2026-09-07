def mask_secret(text: str, keep: int = 4) -> str:
    if not isinstance(text, str):
        raise TypeError("text must be a str")
    if not isinstance(keep, int):
        raise TypeError("keep must be an int")
    if keep < 0 or keep >= len(text):
        raise ValueError("keep must satisfy 0 <= keep < len(text)")
    return "*" * (len(text) - keep) + text[len(text) - keep :]
