import pytest

from converter.weight import convert_weight


def test_kg_to_lb_rounded():
    assert convert_weight(1, "kg", "lb", decimals=2) == 2.2


def test_zero_weight_boundary():
    assert convert_weight(0, "t", "g") == 0


def test_text_input_raises_type_error():
    with pytest.raises(TypeError):
        convert_weight("ten", "kg", "g")

def test_negative_weight_raises():
    with pytest.raises(ValueError):
        convert_weight(-1, "kg", "g")