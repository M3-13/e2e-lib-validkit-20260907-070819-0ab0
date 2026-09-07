import pytest

from validkit.iban import is_valid_iban


def test_valid_iban_with_spaces():
    assert is_valid_iban("DE89 3704 0044 0532 0130 00") is True


def test_valid_iban_without_spaces():
    assert is_valid_iban("DE89370400440532013000") is True


def test_valid_iban_lowercase():
    assert is_valid_iban("de89 3704 0044 0532 0130 00") is True


@pytest.mark.parametrize(
    "iban",
    [
        "GB82 WEST 1234 5698 7654 32",
        "NL91 ABNA 0417 1643 00",
        "FR14 2004 1010 0505 0001 3M02 606",
        "NO93 8601 1117 947",
    ],
)
def test_valid_ibans_from_other_countries(iban):
    assert is_valid_iban(iban) is True


def test_manipulated_check_digit_is_invalid():
    assert is_valid_iban("DE89370400440532013001") is False


def test_manipulated_character_is_invalid():
    assert is_valid_iban("DE89 3704 0044 0532 0130 0X") is False


def test_too_short_iban_is_invalid():
    assert is_valid_iban("DE89") is False
    assert is_valid_iban("DE8937040044") is False


def test_too_long_iban_is_invalid():
    assert is_valid_iban("DE89" + "3704" * 9) is False


def test_empty_string_is_invalid():
    assert is_valid_iban("") is False


def test_disallowed_characters_raise_value_error():
    with pytest.raises(ValueError):
        is_valid_iban("DE89-3704-0044-0532-0130-00")
    with pytest.raises(ValueError):
        is_valid_iban("DE89 3704 0044 0532 0130 00!")


def test_non_str_raises_type_error():
    with pytest.raises(TypeError):
        is_valid_iban(123456789)
    with pytest.raises(TypeError):
        is_valid_iban(None)


def test_is_valid_iban_is_silent(capsys):
    is_valid_iban("DE89 3704 0044 0532 0130 00")
    is_valid_iban("DE89370400440532013001")
    with pytest.raises(ValueError):
        is_valid_iban("DE89-3704")
    with pytest.raises(TypeError):
        is_valid_iban(42)
    captured = capsys.readouterr()
    assert captured.out == ""
    assert captured.err == ""
