from __future__ import annotations


def clamp(value: float | int, low: float | int, high: float | int) -> float | int:
    for name, arg in (("value", value), ("low", low), ("high", high)):
        if isinstance(arg, bool) or not isinstance(arg, (int, float)):
            raise TypeError(f"{name} muss int oder float sein")

    if low > high:
        raise ValueError("low darf nicht größer als high sein")

    if value < low:
        return low
    if value > high:
        return high
    return value
