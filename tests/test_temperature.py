import pytest

from converter.temperature import convert_temperature


def test_boiling_point_c_to_f():
    assert convert_temperature(100, "C", "F") == pytest.approx(212)


def test_freezing_point_f_to_c():
    assert convert_temperature(32, "F", "C") == pytest.approx(0)


def test_absolute_zero_boundary_is_allowed():
    assert convert_temperature(0, "K", "C") == pytest.approx(-273.15)


def test_below_absolute_zero_raises():
    with pytest.raises(ValueError):
        convert_temperature(-300, "C", "K")