"""Feature C: weight conversion (owner: Mohammed Taha Mtouri)."""

# Factor to convert one unit into grams
UNITS = {
    "g": 1.0,
    "kg": 1000.0,
    "t": 1_000_000.0,
    "oz": 28.349523125,
    "lb": 453.59237,
}


def convert_weight(value, from_unit, to_unit, decimals=None):
    """Convert a weight; optionally round the result to decimals places."""
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise TypeError("value must be a number")
    if value < 0:
        raise ValueError("weight cannot be negative")
    if from_unit not in UNITS or to_unit not in UNITS:
        raise ValueError(f"unsupported unit: {from_unit} or {to_unit}")
    result = value * UNITS[from_unit] / UNITS[to_unit]
    return round(result, decimals) if decimals is not None else result