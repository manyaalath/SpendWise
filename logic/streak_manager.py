"""
Streak Manager Module
Manages daily spending streak (consecutive days under limit).
"""

import json
import os
from datetime import datetime, timedelta


def get_streak_file_path():
    """
    Get the full path to streak.json file.
    
    Returns:
        str: Absolute path to streak.json
    """
    # Get the directory where this file is located
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # Go up one level to project root, then into data folder
    project_root = os.path.dirname(current_dir)
    data_dir = os.path.join(project_root, 'data')
    
    # Create data directory if it doesn't exist
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
    
    return os.path.join(data_dir, 'streak.json')


def load_streak_data():
    """
    Load streak data from JSON file.
    
    Returns:
        dict: Dictionary with 'current_streak' and 'last_update_date' keys
    """
    file_path = get_streak_file_path()
    
    # Default streak data
    default_data = {
        'current_streak': 0,
        'last_update_date': None,
        'best_streak': 0
    }
    
    # If file doesn't exist, create it with defaults
    if not os.path.exists(file_path):
        save_streak_data(default_data)
        return default_data
    
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            # Ensure all required keys exist
            if 'current_streak' not in data:
                data['current_streak'] = 0
            if 'last_update_date' not in data:
                data['last_update_date'] = None
            if 'best_streak' not in data:
                data['best_streak'] = 0
            return data
    except (json.JSONDecodeError, IOError):
        # If file is corrupted, return default
        return default_data


def save_streak_data(streak_data):
    """
    Save streak data to JSON file.
    
    Args:
        streak_data (dict): Streak data dictionary to save
    """
    file_path = get_streak_file_path()
    
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(streak_data, file, indent=2, ensure_ascii=False)
    except IOError as e:
        print(f"Error saving streak data: {e}")


def get_current_streak():
    """
    Get the current streak count.
    
    Returns:
        int: Current streak of days under limit
    """
    data = load_streak_data()
    return data.get('current_streak', 0)


def get_best_streak():
    """
    Get the best (longest) streak ever achieved.
    
    Returns:
        int: Best streak record
    """
    data = load_streak_data()
    return data.get('best_streak', 0)


def update_streak(is_under_limit):
    """
    Update the streak based on today's spending.
    
    Args:
        is_under_limit (bool): True if today's total is <= daily limit
        
    Returns:
        dict: Updated streak data with 'current_streak', 'best_streak', 'streak_broken' keys
    """
    data = load_streak_data()
    today = datetime.now().strftime('%Y-%m-%d')
    last_update = data.get('last_update_date')
    
    # Check if this is a new day
    # We should only update streak once per day
    if last_update == today:
        # Already updated today, just return current data
        return {
            'current_streak': data['current_streak'],
            'best_streak': data['best_streak'],
            'streak_broken': False,
            'already_updated': True
        }
    
    streak_broken = False
    
    # Check if we missed a day (streak should break if gap > 1 day)
    if last_update is not None:
        last_date = datetime.strptime(last_update, '%Y-%m-%d')
        today_date = datetime.strptime(today, '%Y-%m-%d')
        days_gap = (today_date - last_date).days
        
        # If gap is more than 1 day, we missed days and streak breaks
        if days_gap > 1:
            data['current_streak'] = 0
            streak_broken = True
    
    # Update streak based on today's performance
    if is_under_limit:
        # Increment streak
        data['current_streak'] += 1
        
        # Update best streak if current is higher
        if data['current_streak'] > data['best_streak']:
            data['best_streak'] = data['current_streak']
    else:
        # Over limit - streak breaks
        data['current_streak'] = 0
        streak_broken = True
    
    # Update last update date
    data['last_update_date'] = today
    
    # Save updated data
    save_streak_data(data)
    
    return {
        'current_streak': data['current_streak'],
        'best_streak': data['best_streak'],
        'streak_broken': streak_broken,
        'already_updated': False
    }


def check_and_update_streak():
    """
    Automatically check today's spending and update streak.
    
    Returns:
        dict: Streak update result
    """
    from logic.daily_tracker import get_today_total
    from logic.limit_checker import get_daily_limit
    
    today_total = get_today_total()
    daily_limit = get_daily_limit()
    
    # Streak continues if spending is at or under limit
    is_under_limit = today_total <= daily_limit
    
    return update_streak(is_under_limit)


if __name__ == "__main__":
    # Simple test
    print("Testing streak manager...")
    
    current = get_current_streak()
    best = get_best_streak()
    
    print(f"Current streak: {current} days")
    print(f"Best streak: {best} days")
    
    # Test updating streak (under limit)
    print("\nTesting streak update (under limit)...")
    result = update_streak(True)
    print(f"  New streak: {result['current_streak']}")
    print(f"  Streak broken: {result['streak_broken']}")
