import io
from contextlib import redirect_stderr, redirect_stdout

from validkit.accents import strip_accents


def test_strip_accents_cafe():
    assert strip_accents("café") == "cafe"


def test_strip_accents_uber():
    assert strip_accents("über") == "uber"


def test_strip_accents_naive():
    assert strip_accents("naïve") == "naive"


def test_strip_accents_already_plain():
    assert strip_accents("cafe") == "cafe"


def test_strip_accents_empty_string():
    assert strip_accents("") == ""


def test_strip_accents_multiple_accents():
    assert strip_accents("Ångström") == "Angstrom"


def test_strip_accents_ligature_unchanged():
    assert strip_accents("œ") == "œ"


def test_strip_accents_non_string_raises_typeerror():
    for bad in (None, 42, 3.14, ["café"], b"cafe"):
        try:
            strip_accents(bad)
        except TypeError:
            pass
        else:
            raise AssertionError(f"expected TypeError for {bad!r}")


def test_strip_accents_writes_nothing_to_stdout_or_stderr():
    stdout = io.StringIO()
    stderr = io.StringIO()
    with redirect_stdout(stdout), redirect_stderr(stderr):
        strip_accents("café über naïve")
    assert stdout.getvalue() == ""
    assert stderr.getvalue() == ""
