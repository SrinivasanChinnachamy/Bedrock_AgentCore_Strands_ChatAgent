from strands import tool

@tool
def celsius_to_fahrenheit(celsius: float):
    """Convert Celsius to Fahrenheit"""
    fahrenheit = (celsius * 9/5) + 32
    return f"{celsius}°C = {fahrenheit}°F"

@tool
def kilometers_to_miles(km: float):
    """Convert kilometers to miles"""
    miles = km * 0.621371
    return f"{km} km = {miles:.2f} miles"