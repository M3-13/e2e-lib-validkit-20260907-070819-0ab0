from validkit import (
    clamp,
    is_valid_email,
    is_valid_iban,
    is_valid_isbn13,
    luhn_check,
    mask_secret,
    normalize_phone,
    slugify,
    strip_accents,
)


def test_all_public_functions_are_importable():
    for name in (
        "is_valid_email",
        "luhn_check",
        "is_valid_iban",
        "is_valid_isbn13",
        "normalize_phone",
        "strip_accents",
        "mask_secret",
        "slugify",
        "clamp",
    ):
        assert name in globals(), name


def test_all_public_functions_are_callable():
    assert callable(is_valid_email)
    assert callable(luhn_check)
    assert callable(is_valid_iban)
    assert callable(is_valid_isbn13)
    assert callable(normalize_phone)
    assert callable(strip_accents)
    assert callable(mask_secret)
    assert callable(slugify)
    assert callable(clamp)
