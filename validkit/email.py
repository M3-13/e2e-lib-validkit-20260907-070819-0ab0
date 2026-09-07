import re

_MAX_EMAIL_LENGTH = 10_000

_LOCAL_PART = r"[A-Za-z0-9.!#$%&'*+/=?^_`{|}~-]+"
_DOMAIN_LABEL = r"[A-Za-z0-9](?:[A-Za-z0-9-]{0,61}[A-Za-z0-9])?"

_EMAIL_RE = re.compile(rf"{_LOCAL_PART}@{_DOMAIN_LABEL}(?:\.{_DOMAIN_LABEL})+")


def is_valid_email(text: str) -> bool:
    if not isinstance(text, str):
        raise TypeError(f"is_valid_email expects str, got {type(text).__name__}")

    if len(text) > _MAX_EMAIL_LENGTH:
        raise ValueError(
            f"is_valid_email text exceeds maximum length of {_MAX_EMAIL_LENGTH} characters"
        )

    return _EMAIL_RE.fullmatch(text) is not None
