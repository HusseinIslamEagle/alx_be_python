# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5


def convert_to_celsius(fahrenheit):
    """Converts Fahrenheit to Celsius using the global factor."""
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR


def convert_to_fahrenheit(celsius):
    """Converts Celsius to Fahrenheit using the global factor."""
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32


# ---- User Interaction ----
try:
    temperature_input = input("Enter the temperature to convert: ")

    # Validate numeric input
    temperature = float(temperature_input)  # لو مش رقم هيعمل error

    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

    if unit == "F":
        result = convert_to_celsius(temperature)
        print(f"{temperature}°F is {result}°C")

    elif unit == "C":
        result = convert_to_fahrenheit(temperature)
        print(f"{temperature}°C is {result}°F")

    else:
        raise ValueError("Invalid unit. Please enter 'C' or 'F'.")

except ValueError:
    raise ValueError("Invalid temperature. Please enter a numeric value.")
