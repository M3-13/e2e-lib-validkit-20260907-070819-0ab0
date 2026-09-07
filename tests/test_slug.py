import pytest

from validkit.slug import slugify


def test_slugify_basic_accents_and_special_chars():
    assert slugify("Héllo Wörld!") == "hello-world"


def test_slugify_lowercases():
    assert slugify("HELLO WORLD") == "hello-world"


def test_slugify_removes_accents():
    assert slugify("café über naïve") == "cafe-uber-naive"


def test_slugify_special_characters_replaced():
    assert slugify("Foo@Bar#Baz") == "foo-bar-baz"


def test_slugify_collapses_multiple_hyphens():
    assert slugify("a -- b -- c") == "a-b-c"


def test_slugify_strips_leading_and_trailing_hyphens():
    assert slugify("--- hello world ---") == "hello-world"


def test_slugify_empty_string():
    assert slugify("") == ""


def test_slugify_wrong_type_raises_typeerror():
    with pytest.raises(TypeError):
        slugify(123)


def test_slugify_too_long_raises_valueerror():
    with pytest.raises(ValueError):
        slugify("a" * 10001)


def test_slugify_max_length_is_accepted():
    assert slugify("a" * 10000) == "a" * 10000


def test_slugify_does_not_write_to_stdout_or_stderr(capsys):
    slugify("Héllo Wörld!")
    captured = capsys.readouterr()
    assert captured.out == ""
    assert captured.err == ""
