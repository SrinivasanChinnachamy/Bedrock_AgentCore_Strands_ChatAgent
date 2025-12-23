from strands import tool
import random

@tool
def random_number(min_val: int = 1, max_val: int = 100):
    """Generate a random number between min_val and max_val"""
    return f"Random number: {random.randint(min_val, max_val)}"

@tool
def random_color():
    """Get a random color name"""
    colors = ["red", "blue", "green", "yellow", "purple", "orange", "pink", "brown", "black", "white"]
    return f"Random color: {random.choice(colors)}"