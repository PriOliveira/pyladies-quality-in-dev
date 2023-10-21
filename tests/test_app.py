import pytest

from src import app as converter


@pytest.mark.parametrize(
    ("value", "expected"),
    [
        (0, 273.15),
        (100, 373.15),
    ],
)
def test_celsius_to_kelvin(value: float, expected: float) -> None:
    assert converter.celsius_to_kelvin(value) == expected


@pytest.mark.parametrize(
    ("value", "expected"),
    [
        (0, 32),
        (100, 212),
    ],
)
def test_celsius_to_fahrenheit(value: float, expected: float) -> None:
    assert converter.celsius_to_fahrenheit(value) == expected


@pytest.mark.parametrize(
    ("unit_from", "unit_to", "temperature", "expected"),
    [
        pytest.param("C", "F", 100, 212, id="celsius_to_fahrenheit"),
        pytest.param("F", "C", 212, 100, id="fahrenheit_to_celsius"),
        pytest.param("C", "K", 0, 273.15, id="celsius_to_kelvin"),
        pytest.param("K", "C", 273.15, 0, id="kelvin_to_celsius"),
        pytest.param("K", "F", 273.15, 32, id="kelvin_to_fahrenheit"),
        pytest.param("F", "K", 32, 273.15, id="fahrenheit_to_kelvin"),
    ],
)
def test_convert_temperature(
    unit_from: converter.TemperatureUnit,
    unit_to: converter.TemperatureUnit,
    temperature: float,
    expected: float,
) -> None:
    result = converter.convert_temperature(
        unit_from=unit_from,
        unit_to=unit_to,
        temperature=temperature,
    )
    assert pytest.approx(result, 0.1) == expected
