"""Feature B: temperature conversion (owner: Rayan Day)."""

ABSOLUTE_ZERO_C = -273.15
UNITS = ("C", "F", "K")


def to_celsius(value, unit):
    if unit == "C":
        return value
    if unit == "F":
        return (value - 32) * 5 / 9
    return value - 273.15


def from_celsius(value, unit):
    if unit == "C":
        return value
    if unit == "F":
        return value * 9 / 5 + 32
    return value + 273.15


def convert_temperature(value, from_unit, to_unit):
    """Convert a temperature between C, F and K."""
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise TypeError("value must be a number")
    if from_unit not in UNITS or to_unit not in UNITS:
        raise ValueError(f"unsupported unit: {from_unit} or {to_unit}")
    celsius = to_celsius(value, from_unit)
    if celsius < ABSOLUTE_ZERO_C - 1e-9:
        raise ValueError("temperature below absolute zero")
    return from_celsius(celsius, to_unit)