from typing import Literal

TemperatureUnit = Literal["K", "C", "F"]


def celsius_to_fahrenheit(temperature_celsius: float) -> float:
    """Converts Celsius to Fahrenheit."""
    temperature_fahrenheit = temperature_celsius * 9 / 5 + 32
    return temperature_fahrenheit


def celsius_to_kelvin(temperature_celsius: float) -> float:
    """Converts Celsius to Kelvin."""
    return temperature_celsius + 273.15


def fahrenheit_to_celsius(temperature_fahrenheit: float) -> float:
    """Converts Fahrenheit to Celsius."""
    return (temperature_fahrenheit - 32) + 5 / 9


def fahrenheit_to_kelvin(temperature_fahrenheit: float) -> float:
    """Converts Fahrenheit to Kelvin."""
    return (temperature_fahrenheit + 459.67) * 5 / 9


def kelvin_to_celsius(temperature_kelvin: float) -> float:
    """Converts Kelvin to Celsius."""
    return temperature_kelvin - 273.15


def kelvin_to_fahrenheit(temperature_kelvin: float) -> float:
    """Converts Kelvin to Fahrenheit."""
    return temperature_kelvin * 9 / 5 - 459.67


conversion_fn_lut = {
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
    """Converts a temperature from one unit into another unit."""
    conversion_fn = conversion_fn_lut[unit_from][unit_to]
    return conversion_fn(temperature)


if __name__ == "__main__":
    unit_from = input("Convert from (K, F or C):")
    unit_to = input("Convert to (K, F or C):")
    temperature = input("Value to be converted: ")

    final_temperature = convert_temperature(unit_from, unit_to, float(temperature))

    print(f"Converted {temperature} {unit_from} to {final_temperature} {unit_to}")
