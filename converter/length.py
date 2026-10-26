"""Feature A: length conversion (owner: Khalil Berjaoui)."""

# Factor to convert one unit into metres
UNITS = {
    "mm": 0.001,
    "cm": 0.01,
    "m": 1.0,
    "km": 1000.0,
    "in": 0.0254,
    "ft": 0.3048,
    "mi": 1609.344,
}


def convert_length(value, from_unit, to_unit):
    """Convert a length between two supported units."""
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise TypeError("value must be a number")
    if value < 0:
        raise ValueError("length cannot be negative")
    if from_unit not in UNITS or to_unit not in UNITS:
        raise ValueError(f"unsupported unit: {from_unit} or {to_unit}")
    return value * UNITS[from_unit] / UNITS[to_unit]