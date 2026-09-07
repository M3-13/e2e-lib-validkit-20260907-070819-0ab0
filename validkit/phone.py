import re

_MAX_LENGTH = 10_000

_COUNTRY_CALLING_CODES = {
    "DE": "49",
}

_SEPARATOR_RE = re.compile(r"[\s\-()./]+")
_DIGITS_RE = re.compile(r"\d+")


def normalize_phone(text: str, country_code: str) -> str:
    """Normalize a phone number to E.164 form: +<calling code><significant digits>.

    Formatting characters (spaces, hyphens, parentheses, dots, slashes) are
    stripped. A leading ``+`` is accepted; without it, a leading ``0`` is treated
    as the national trunk prefix and removed. Unsupported country codes and
    malformed input raise ``ValueError``; a non-string argument raises
    ``TypeError``.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a str")
    if not isinstance(country_code, str):
        raise TypeError("country_code must be a str")

    if len(text) > _MAX_LENGTH:
        raise ValueError(f"text must be at most {_MAX_LENGTH} characters")

    country = country_code.upper()
    calling_code = _COUNTRY_CALLING_CODES.get(country)
    if calling_code is None:
        raise ValueError(f"unsupported country code: {country_code!r}")

    value = text.strip()
    if not value:
        raise ValueError("phone number must not be empty")

    has_prefix = value.startswith("+")
    if has_prefix:
        value = value[1:]
    if "+" in value:
        raise ValueError("'+' may only appear at the start of the phone number")

    value = _SEPARATOR_RE.sub("", value)

    if not value:
        raise ValueError("phone number contains no digits")
    if _DIGITS_RE.fullmatch(value) is None:
        raise ValueError("phone number contains invalid characters")

    if has_prefix:
        if not value.startswith(calling_code):
            raise ValueError(f"phone number does not match the calling code for {country}")
        national = value[len(calling_code) :]
    else:
        national = value

    national = national.lstrip("0")
    if not national:
        raise ValueError("phone number has no significant digits")

    return "+" + calling_code + national
