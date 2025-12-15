"""
Function 5: Date/time utility.
"""


def function_five(days: int = 0) -> str:
    """
    Get a formatted date string for a date N days from today.

    Args:
        days: Number of days to add (can be negative for past dates).
               Default is 0 (today).

    Returns:
        A formatted date string in YYYY-MM-DD format.

    Example:
        >>> function_five(0)  # Today
        '2025-01-13'
        >>> function_five(7)  # One week from today
        '2025-01-20'
        >>> function_five(-1)  # Yesterday
        '2025-01-12'
    """
    from datetime import datetime, timedelta

    target_date = datetime.now() + timedelta(days=days)
    return target_date.strftime("%Y-%m-%d")

