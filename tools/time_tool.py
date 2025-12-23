from strands import tool
from datetime import datetime, timezone, timedelta

@tool
def get_time():
    """Get current date and time in GMT+5:30 (IST)"""
    ist = timezone(timedelta(hours=5, minutes=30))
    return datetime.now(ist).strftime("%Y-%m-%d %H:%M:%S IST")