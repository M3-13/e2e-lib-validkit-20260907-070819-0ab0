from __future__ import annotations

import io
from contextlib import redirect_stderr, redirect_stdout

import pytest

from validkit.clamp import clamp


def test_clamp_above_high():
    assert clamp(15, 0, 10) == 10


def test_clamp_below_low():
    assert clamp(-5, 0, 10) == 0


def test_clamp_within_bounds():
    assert clamp(5, 0, 10) == 5


def test_clamp_preserves_int_type():
    result = clamp(15, 0, 10)
    assert result == 10
    assert isinstance(result, int)


def test_clamp_preserves_float_type():
    result = clamp(15.5, 0.0, 10.0)
    assert result == 10.0
    assert isinstance(result, float)


def test_clamp_lower_boundary():
    assert clamp(0, 0, 10) == 0


def test_clamp_upper_boundary():
    assert clamp(10, 0, 10) == 10


def test_clamp_low_equals_high():
    assert clamp(7, 5, 5) == 5


def test_clamp_negative_bounds():
    assert clamp(-3, -10, -1) == -3


def test_clamp_low_greater_than_high_raises_value_error():
    with pytest.raises(ValueError):
        clamp(5, 10, 0)


def test_clamp_non_numeric_value_raises_type_error():
    with pytest.raises(TypeError):
        clamp("5", 0, 10)


def test_clamp_non_numeric_low_raises_type_error():
    with pytest.raises(TypeError):
        clamp(5, None, 10)


def test_clamp_non_numeric_high_raises_type_error():
    with pytest.raises(TypeError):
        clamp(5, 0, "10")


def test_clamp_bool_value_raises_type_error():
    with pytest.raises(TypeError):
        clamp(True, 0, 10)


def test_clamp_writes_nothing_to_stdout_or_stderr():
    stdout = io.StringIO()
    stderr = io.StringIO()
    with redirect_stdout(stdout), redirect_stderr(stderr):
        clamp(15, 0, 10)
        clamp(-5, 0, 10)
        clamp(5, 0, 10)
    assert stdout.getvalue() == ""
    assert stderr.getvalue() == ""
