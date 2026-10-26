import pytest

from converter.length import convert_length


def test_km_to_m():
    assert convert_length(2, "km", "m") == pytest.approx(2000)


def test_zero_and_same_unit_boundary():
    assert convert_length(0, "mi", "cm") == 0
    assert convert_length(5, "ft", "ft") == pytest.approx(5)


def test_unknown_unit_raises():
    with pytest.raises(ValueError):
        convert_length(1, "km", "parsec")


def test_negative_length_raises():
    with pytest.raises(ValueError):
        convert_length(-3, "m", "cm")