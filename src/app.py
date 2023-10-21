"""Temperature conversion."""

import logging
from collections.abc import Callable
from typing import Literal, cast

TemperatureUnit = Literal["K", "C", "F"]


def celsius_to_fahrenheit(temperature_celsius: float) -> float:
    """Convert Celsius to Fahrenheit."""
    return temperature_celsius * 9 / 5 + 32


def celsius_to_kelvin(temperature_celsius: float) -> float:
    """Convert Celsius to Kelvin."""
    return temperature_celsius + 273.15


def fahrenheit_to_celsius(temperature_fahrenheit: float) -> float:
    """Convert Fahrenheit to Celsius."""
    return (temperature_fahrenheit - 32) * 5 / 9


def fahrenheit_to_kelvin(temperature_fahrenheit: float) -> float:
    """Convert Fahrenheit to Kelvin."""
    return (temperature_fahrenheit + 459.67) * 5 / 9


def kelvin_to_celsius(temperature_kelvin: float) -> float:
    """Convert Kelvin to Celsius."""
    return temperature_kelvin - 273.15


def kelvin_to_fahrenheit(temperature_kelvin: float) -> float:
    """Convert Kelvin to Fahrenheit."""
    return temperature_kelvin * 9 / 5 - 459.67


conversion_fn_lut: dict[TemperatureUnit, dict[TemperatureUnit, Callable[[float], float]]] = {
    "C": {
        "F": celsius_to_fahrenheit,
        "K": celsius_to_kelvin,
    },
    "F": {
        "C": fahrenheit_to_celsius,
        "K": fahrenheit_to_kelvin,
    },
    "K": {
        "C": kelvin_to_celsius,
        "F": kelvin_to_fahrenheit,
    },
}


def convert_temperature(
    unit_from: TemperatureUnit,
    unit_to: TemperatureUnit,
    temperature: float,
) -> float:
    """Convert a temperature from one unit into another unit."""
    conversion_fn = conversion_fn_lut[unit_from][unit_to]
    return conversion_fn(temperature)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    unit_from = input("Convert from (K, F or C):")
    unit_to = input("Convert to (K, F or C):")
    temperature = input("Value to be converted: ")

    final_temperature = convert_temperature(
        cast(TemperatureUnit, unit_from),
        cast(TemperatureUnit, unit_to),
        float(temperature),
    )
    data = {
        "temperature": temperature,
        "unit_from": unit_from,
        "final_temperature": final_temperature,
        "unit_to": unit_to,
    }
    template = "Converted successfully: %(temperature)s%(unit_from)s to %(final_temperature).2f%(unit_to)s"
    message = template % data
    logging.info(message)
