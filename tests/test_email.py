import pytest

from validkit import is_valid_email


def test_valid_simple_email():
    assert is_valid_email("user@example.com") is True


def test_valid_email_with_subdomain():
    assert is_valid_email("user@mail.example.com") is True


def test_valid_email_with_dots_and_plus_in_local_part():
    assert is_valid_email("first.last+tag@example.co.uk") is True


def test_missing_domain_returns_false():
    assert is_valid_email("kein@") is False


def test_missing_local_part_returns_false():
    assert is_valid_email("@example.com") is False


def test_whitespace_in_local_part_returns_false():
    assert is_valid_email("a b@c.de") is False


def test_missing_at_returns_false():
    assert is_valid_email("user.example.com") is False


def test_empty_string_returns_false():
    assert is_valid_email("") is False


def test_consecutive_dots_in_domain_returns_false():
    assert is_valid_email("user@example..com") is False


def test_domain_without_tld_returns_false():
    assert is_valid_email("user@example") is False


def test_leading_at_returns_false():
    assert is_valid_email("@") is False


@pytest.mark.parametrize("value", [None, 42, 4.2, ["user@example.com"], ("user@example.com",)])
def test_wrong_type_raises_type_error(value):
    with pytest.raises(TypeError):
        is_valid_email(value)


def test_overlong_input_raises_value_error():
    too_long = "a" * 10_001 + "@example.com"
    with pytest.raises(ValueError):
        is_valid_email(too_long)


def test_exactly_at_limit_is_processed():
    local = "a" * (10_000 - len("@example.com"))
    assert is_valid_email(local + "@example.com") is True


def test_does_not_write_to_stdout_or_stderr(capsys):
    is_valid_email("user@example.com")
    is_valid_email("kein@")
    is_valid_email("@example.com")
    is_valid_email("a b@c.de")
    captured = capsys.readouterr()
    assert captured.out == ""
    assert captured.err == ""
