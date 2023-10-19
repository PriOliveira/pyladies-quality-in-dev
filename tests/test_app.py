import pytest

from src import app as converter


@pytest.mark.parametrize(
    "value, expected",
    [
        (0, 273.15),
        (100, 373.15),
    ],
)
def test_celsius_to_kelvin(value: float, expected: float):
    assert converter.celsius_to_kelvin(value) == expected


@pytest.mark.parametrize(
    "value, expected",
    [
        (0, 32),
        (100, 212),
    ],
)
def test_celsius_to_fahrenheit(value: float, expected: float):
    assert converter.celsius_to_fahrenheit(value) == expected


@pytest.mark.parametrize(
    "unit_from, unit_to, temperature, expected",
    [
        ("C", "F", 100, 212),
        ("C", "K", 0, 273.15),
    ],
)
def test_convert_temperature(
    unit_from: converter.TemperatureUnit,
    unit_to: converter.TemperatureUnit,
    temperature: float,
    expected: float,
):
    result = converter.convert_temperature(
        unit_from=unit_from,
        unit_to=unit_to,
        temperature=temperature,
    )
    assert result == expected
