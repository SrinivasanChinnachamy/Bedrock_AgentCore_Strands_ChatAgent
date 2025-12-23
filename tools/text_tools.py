from strands import tool

@tool
def text_length(text: str):
    """Count characters in text"""
    return f"Text length: {len(text)} characters"

@tool
def reverse_text(text: str):
    """Reverse the given text"""
    return f"Reversed text: {text[::-1]}"