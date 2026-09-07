import re
import unicodedata


def slugify(text: str) -> str:
    if not isinstance(text, str):
        raise TypeError("text must be a str")

    if len(text) > 10000:
        raise ValueError("text must be at most 10000 characters")

    normalized = unicodedata.normalize("NFD", text)
    without_accents = "".join(ch for ch in normalized if not unicodedata.combining(ch))
    lowered = without_accents.lower()
    slug = re.sub(r"[^\w]+", "-", lowered)
    return slug.strip("-")
