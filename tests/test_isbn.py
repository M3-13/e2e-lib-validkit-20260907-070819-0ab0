import pytest

from validkit import is_valid_isbn13


def test_valid_isbn13_with_hyphens():
    assert is_valid_isbn13("978-3-16-148410-0") is True


def test_valid_isbn13_plain_digits():
    assert is_valid_isbn13("9783161484100") is True


def test_valid_isbn13_with_spaces():
    assert is_valid_isbn13("978 3 16 148410 0") is True


def test_valid_isbn13_second_example():
    assert is_valid_isbn13("978-0-306-40615-7") is True


def test_wrong_check_digit_returns_false():
    assert is_valid_isbn13("978-3-16-148410-1") is False


def test_wrong_check_digit_plain():
    assert is_valid_isbn13("9783161484101") is False


def test_tolerates_mixed_separators():
    assert is_valid_isbn13("978-3 16 148410-0") is True


def test_too_short_returns_false():
    assert is_valid_isbn13("978-3-16-14841") is False


def test_too_long_returns_false():
    assert is_valid_isbn13("978-3-16-148410-00") is False


def test_empty_string_returns_false():
    assert is_valid_isbn13("") is False


def test_non_digit_character_returns_false():
    assert is_valid_isbn13("978-3-16-148410-X") is False


def test_only_separators_returns_false():
    assert is_valid_isbn13("---   ") is False


@pytest.mark.parametrize("value", [None, 9783161484100, ["9783161484100"], 9.78])
def test_wrong_type_raises_type_error(value):
    with pytest.raises(TypeError):
        is_valid_isbn13(value)


def test_does_not_write_to_stdout_or_stderr(capsys):
    is_valid_isbn13("978-3-16-148410-0")
    is_valid_isbn13("978-3-16-148410-1")
    is_valid_isbn13("not an isbn")
    captured = capsys.readouterr()
    assert captured.out == ""
    assert captured.err == ""
