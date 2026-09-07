import pytest

from validkit.phone import normalize_phone


def test_international_prefix_with_spaces():
    assert normalize_phone("+49 170 1234567", "DE") == "+491701234567"


def test_national_with_leading_zero():
    assert normalize_phone("0170 1234567", "DE") == "+491701234567"


def test_international_prefix_without_spaces():
    assert normalize_phone("+491701234567", "DE") == "+491701234567"


def test_separators_are_stripped():
    assert normalize_phone("0170-123-4567", "DE") == "+491701234567"
    assert normalize_phone("(0170) 123.45.67", "DE") == "+491701234567"
    assert normalize_phone("0170 / 1234567", "DE") == "+491701234567"


def test_country_code_is_case_insensitive():
    assert normalize_phone("0170 1234567", "de") == "+491701234567"


def test_international_prefix_with_trunk_zero():
    assert normalize_phone("+490170 1234567", "DE") == "+491701234567"


def test_unsupported_country_code_raises_value_error():
    with pytest.raises(ValueError):
        normalize_phone("0170 1234567", "US")


def test_empty_input_raises_value_error():
    with pytest.raises(ValueError):
        normalize_phone("", "DE")


def test_letters_raise_value_error():
    with pytest.raises(ValueError):
        normalize_phone("0170 abc", "DE")


def test_plus_in_middle_raises_value_error():
    with pytest.raises(ValueError):
        normalize_phone("0170+1234567", "DE")


def test_prefix_mismatch_raises_value_error():
    with pytest.raises(ValueError):
        normalize_phone("+1 202 555 0100", "DE")


def test_no_significant_digits_raises_value_error():
    with pytest.raises(ValueError):
        normalize_phone("+49", "DE")
    with pytest.raises(ValueError):
        normalize_phone("000", "DE")


def test_non_string_text_raises_type_error():
    with pytest.raises(TypeError):
        normalize_phone(170, "DE")  # type: ignore[arg-type]
    with pytest.raises(TypeError):
        normalize_phone(None, "DE")  # type: ignore[arg-type]
    with pytest.raises(TypeError):
        normalize_phone(["0170"], "DE")  # type: ignore[arg-type]


def test_non_string_country_code_raises_type_error():
    with pytest.raises(TypeError):
        normalize_phone("0170 1234567", None)  # type: ignore[arg-type]
    with pytest.raises(TypeError):
        normalize_phone("0170 1234567", 49)  # type: ignore[arg-type]


def test_length_over_limit_raises_value_error():
    with pytest.raises(ValueError):
        normalize_phone("0" * 10_001, "DE")


def test_length_at_limit_is_accepted():
    result = normalize_phone("1" * 10_000, "DE")
    assert result == "+49" + "1" * 10_000


def test_no_stdout_or_stderr(capsys):
    normalize_phone("+49 170 1234567", "DE")
    normalize_phone("0170 1234567", "DE")
    with pytest.raises(ValueError):
        normalize_phone("0170 abc", "DE")
    with pytest.raises(TypeError):
        normalize_phone(170, "DE")  # type: ignore[arg-type]

    captured = capsys.readouterr()
    assert captured.out == ""
    assert captured.err == ""
