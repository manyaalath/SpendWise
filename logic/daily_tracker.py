"""
Daily Tracker Module
Calculates daily spending totals.
"""

from datetime import datetime
from logic.expense_store import get_today_expenses, get_expenses_for_date


def get_daily_total(date_str=None):
    """
    Get total spending for a specific date.
    
    Args:
        date_str (str, optional): Date in YYYY-MM-DD format. 
                                  If None, uses today's date.
    
    Returns:
        int: Total amount spent on that date
    """
    if date_str is None:
        # Use today's date
        expenses = get_today_expenses()
    else:
        # Use specified date
        expenses = get_expenses_for_date(date_str)
    
    # Sum all expenses for the date
    # If no expenses, sum returns 0
    total = sum(expenses)
    
    return total


def get_today_total():
    """
    Get total spending for today.
    
    Returns:
        int: Total amount spent today
    """
    return get_daily_total()


def get_expense_count(date_str=None):
    """
    Get number of expenses for a specific date.
    
    Args:
        date_str (str, optional): Date in YYYY-MM-DD format.
                                  If None, uses today's date.
    
    Returns:
        int: Number of expenses on that date
    """
    if date_str is None:
        expenses = get_today_expenses()
    else:
        expenses = get_expenses_for_date(date_str)
    
    return len(expenses)


def get_today_summary():
    """
    Get a summary of today's spending.
    
    Returns:
        dict: Dictionary with 'total', 'count', and 'expenses' keys
    """
    expenses = get_today_expenses()
    
    return {
        'total': sum(expenses),
        'count': len(expenses),
        'expenses': expenses
    }


if __name__ == "__main__":
    # Simple test
    print("Testing daily tracker...")
    
    summary = get_today_summary()
    print(f"Today's total: ₹{summary['total']}")
    print(f"Number of expenses: {summary['count']}")
    print(f"Expenses: {summary['expenses']}")
