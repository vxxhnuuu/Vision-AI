from datetime import datetime

def get_current_time():
    """Return the current time in a readable format."""
    now = datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")
