import pytest

from validkit import luhn_check


def test_valid_luhn_number():
    assert luhn_check("79927398713") is True


def test_valid_luhn_number_second_example():
    assert luhn_check("49927398716") is True


def test_manipulated_check_digit_returns_false():
    assert luhn_check("79927398714") is False


def test_manipulated_check_digit_second_example():
    assert luhn_check("49927398715") is False


def test_single_zero_is_valid():
    assert luhn_check("0") is True


def test_single_non_zero_digit_is_invalid():
    assert luhn_check("5") is False


def test_empty_string_returns_false():
    assert luhn_check("") is False


def test_non_digit_character_raises_value_error():
    with pytest.raises(ValueError):
        luhn_check("7992739871X")


def test_alphabetic_input_raises_value_error():
    with pytest.raises(ValueError):
        luhn_check("abc")


def test_input_with_spaces_raises_value_error():
    with pytest.raises(ValueError):
        luhn_check("7992 7398 713")


@pytest.mark.parametrize("value", [None, 79927398713, ["79927398713"], 7.9])
def test_wrong_type_raises_type_error(value):
    with pytest.raises(TypeError):
        luhn_check(value)


def test_does_not_write_to_stdout_or_stderr(capsys):
    luhn_check("79927398713")
    luhn_check("79927398714")
    with pytest.raises(ValueError):
        luhn_check("not digits")
    with pytest.raises(TypeError):
        luhn_check(123)
    captured = capsys.readouterr()
    assert captured.out == ""
    assert captured.err == ""
