"""
Expense Store Module
Handles saving and loading expenses from JSON file.
"""

import json
import os
from datetime import datetime


def get_data_dir():
    """
    Get the absolute path to the data directory.
    
    Returns:
        str: Absolute path to data directory
    """
    # Get the directory where this file is located
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # Go up one level to project root, then into data folder
    project_root = os.path.dirname(current_dir)
    data_dir = os.path.join(project_root, 'data')
    
    # Create data directory if it doesn't exist
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
    
    return data_dir


def get_expenses_file_path():
    """
    Get the full path to expenses.json file.
    
    Returns:
        str: Absolute path to expenses.json
    """
    return os.path.join(get_data_dir(), 'expenses.json')


def load_expenses():
    """
    Load expenses from JSON file.
    
    Returns:
        dict: Dictionary with dates as keys and lists of expenses as values
              Example: {"2026-01-18": [299, 120, 50]}
    """
    file_path = get_expenses_file_path()
    
    # If file doesn't exist, return empty dictionary
    if not os.path.exists(file_path):
        return {}
    
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            return data
    except (json.JSONDecodeError, IOError):
        # If file is corrupted or can't be read, return empty dict
        return {}


def save_expenses(expenses_data):
    """
    Save expenses to JSON file.
    
    Args:
        expenses_data (dict): Dictionary of expenses to save
    """
    file_path = get_expenses_file_path()
    
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(expenses_data, file, indent=2, ensure_ascii=False)
    except IOError as e:
        print(f"Error saving expenses: {e}")


def add_expense(amount):
    """
    Add a new expense for today.
    
    Args:
        amount (int): Expense amount to add
        
    Returns:
        bool: True if expense was added successfully, False otherwise
    """
    if amount is None or amount <= 0:
        return False
    
    # Get today's date in YYYY-MM-DD format
    today = datetime.now().strftime('%Y-%m-%d')
    
    # Load existing expenses
    expenses = load_expenses()
    
    # Add today's date if it doesn't exist
    if today not in expenses:
        expenses[today] = []
    
    # Append the new expense
    expenses[today].append(amount)
    
    # Save back to file
    save_expenses(expenses)
    
    return True


def get_expenses_for_date(date_str):
    """
    Get all expenses for a specific date.
    
    Args:
        date_str (str): Date in YYYY-MM-DD format
        
    Returns:
        list: List of expense amounts for that date
    """
    expenses = load_expenses()
    return expenses.get(date_str, [])


def get_today_expenses():
    """
    Get all expenses for today.
    
    Returns:
        list: List of expense amounts for today
    """
    today = datetime.now().strftime('%Y-%m-%d')
    return get_expenses_for_date(today)


if __name__ == "__main__":
    # Simple test
    print("Testing expense store...")
    print(f"Data directory: {get_data_dir()}")
    print(f"Expenses file: {get_expenses_file_path()}")
    
    # Test adding expense
    if add_expense(100):
        print("Added test expense: 100")
    
    # Test reading today's expenses
    today_expenses = get_today_expenses()
    print(f"Today's expenses: {today_expenses}")
