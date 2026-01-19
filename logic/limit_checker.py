"""
Limit Checker Module
Checks if daily spending is approaching or exceeding the limit.
"""

import json
import os


def get_config_file_path():
    """
    Get the full path to config.json file.
    
    Returns:
        str: Absolute path to config.json
    """
    # Get the directory where this file is located
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # Go up one level to project root, then into data folder
    project_root = os.path.dirname(current_dir)
    data_dir = os.path.join(project_root, 'data')
    
    # Create data directory if it doesn't exist
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
    
    return os.path.join(data_dir, 'config.json')


def load_config():
    """
    Load configuration from config.json file.
    
    Returns:
        dict: Configuration dictionary with 'daily_limit' key
    """
    file_path = get_config_file_path()
    
    # Default configuration
    default_config = {
        'daily_limit': 500
    }
    
    # If file doesn't exist, create it with defaults
    if not os.path.exists(file_path):
        save_config(default_config)
        return default_config
    
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            config = json.load(file)
            # Ensure daily_limit exists
            if 'daily_limit' not in config:
                config['daily_limit'] = 500
            return config
    except (json.JSONDecodeError, IOError):
        # If file is corrupted, return default
        return default_config


def save_config(config):
    """
    Save configuration to config.json file.
    
    Args:
        config (dict): Configuration dictionary to save
    """
    file_path = get_config_file_path()
    
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(config, file, indent=2, ensure_ascii=False)
    except IOError as e:
        print(f"Error saving config: {e}")


def get_daily_limit():
    """
    Get the daily spending limit.
    
    Returns:
        int: Daily spending limit in rupees
    """
    config = load_config()
    return config.get('daily_limit', 500)


def set_daily_limit(new_limit):
    """
    Update the daily spending limit.
    
    Args:
        new_limit (int): New daily limit to set
        
    Returns:
        bool: True if limit was updated successfully
    """
    if new_limit <= 0:
        return False
    
    config = load_config()
    config['daily_limit'] = new_limit
    save_config(config)
    
    return True


def check_limit(daily_total):
    """
    Check if daily spending is near or over the limit.
    
    Args:
        daily_total (int): Total amount spent today
        
    Returns:
        dict: Dictionary with 'warning', 'exceeded', 'limit', 'percentage' keys
              - warning: True if >= 80% of limit
              - exceeded: True if over limit
              - limit: The daily limit value
              - percentage: Percentage of limit used
    """
    limit = get_daily_limit()
    
    # Calculate percentage of limit used
    if limit > 0:
        percentage = (daily_total / limit) * 100
    else:
        percentage = 0
    
    # Warning if at 80% or more of limit
    warning = daily_total >= (limit * 0.8)
    
    # Exceeded if over limit
    exceeded = daily_total > limit
    
    return {
        'warning': warning,
        'exceeded': exceeded,
        'limit': limit,
        'percentage': round(percentage, 1)
    }


def get_remaining_budget():
    """
    Get remaining budget for today.
    
    Args:
        daily_total (int): Total amount spent today
        
    Returns:
        int: Remaining budget (can be negative if over limit)
    """
    from logic.daily_tracker import get_today_total
    
    limit = get_daily_limit()
    today_total = get_today_total()
    remaining = limit - today_total
    
    return remaining


if __name__ == "__main__":
    # Simple test
    print("Testing limit checker...")
    
    limit = get_daily_limit()
    print(f"Daily limit: ₹{limit}")
    
    # Test with different amounts
    test_amounts = [100, 400, 450, 600]
    
    for amount in test_amounts:
        result = check_limit(amount)
        print(f"\nAmount: ₹{amount}")
        print(f"  Warning: {result['warning']}")
        print(f"  Exceeded: {result['exceeded']}")
        print(f"  Percentage: {result['percentage']}%")
