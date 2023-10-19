import pytest

from src.app import c_to_f, c_to_k


@pytest.mark.parametrize(
    "value, expected",
    [
        (0, 273.15),
        (100, 373.15),
    ],
)
def test_c_to_k(value: float, expected: float):
    assert c_to_k(value) == expected


@pytest.mark.parametrize(
    "value, expected",
    [
        (0, 32),
        (100, 212),
    ],
)
def test_c_to_f(value: float, expected: float):
    assert c_to_f(value) == expected
