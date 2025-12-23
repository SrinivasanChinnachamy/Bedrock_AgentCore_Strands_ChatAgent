from strands import tool
import random

@tool
def weather():
    """Get weather information"""
    conditions = ["sunny", "cloudy", "rainy", "partly cloudy", "windy"]
    temp = random.randint(15, 35)
    condition = random.choice(conditions)
    return f"Current weather: {condition}, {temp}°C"