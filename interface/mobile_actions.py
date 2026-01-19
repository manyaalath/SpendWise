"""
Mobile Actions Module (STUB)
This is a placeholder for future mobile integration.
For now, it returns sample data to test the system.

NOTE: In production, this will be replaced with actual Android/iOS integration
using Droidrun or similar mobile automation tools.
"""

import random
# from droidrun.device import AndroidDevice



def get_latest_sms():
    """
    Get the latest SMS message (STUB).
    
    In production: This will read actual SMS from the phone.
    For now: Returns a sample bank SMS for testing.
    
    Returns:
        str: SMS text content
    """
    # Sample SMS messages for testing
    sample_messages = [
        "₹299 debited from your account ending 1234 for Amazon purchase. Available balance: ₹5000",
        "Rs.120 spent via UPI to Zomato. Transaction ID: 123456789",
        "Rs 150 spent at Flipkart using card ending 5678",
        "INR 200 paid to Uber. Thank you for using our service",
        "₹75 debited for Spotify subscription",
    ]
    
    # Return a random sample SMS
    return random.choice(sample_messages)

    # Future implementation using Droidrun
    # device = AndroidDevice()
    # device.open_app("Messages")
    # device.tap_first_element()
    # message_text = device.read_last_text()
    # return message_text



def send_notification(title, message):
    """
    Send a notification to the phone (STUB).
    
    In production: This will send actual notifications to the mobile device.
    For now: Just prints to console.
    
    Args:
        title (str): Notification title
        message (str): Notification message
    """
    # For now, just print to console
    print(f"\n📱 NOTIFICATION")
    print(f"   Title: {title}")
    print(f"   Message: {message}")
    print()


def get_phone_battery():
    """
    Get phone battery level (STUB).
    
    In production: This will return actual battery level.
    For now: Returns a dummy value.
    
    Returns:
        int: Battery percentage (0-100)
    """
    return 85  # Dummy battery level


def is_screen_on():
    """
    Check if phone screen is on (STUB).
    
    In production: This will check actual screen state.
    For now: Returns True.
    
    Returns:
        bool: True if screen is on, False otherwise
    """
    return True


# Future integration notes:
# --------------------------
# 1. get_latest_sms() will use Android SMS API or Droidrun to read actual messages
# 2. send_notification() will use Android notification API to show real notifications
# 3. Additional functions can be added for:
#    - Reading all SMS from today
#    - Filtering SMS by sender
#    - Auto-categorizing expenses
#    - Setting reminders/alarms


if __name__ == "__main__":
    # Test the stub functions
    print("Testing mobile actions (STUB)...")
    
    sms = get_latest_sms()
    print(f"✓ Sample SMS: {sms}")
    
    send_notification("Test", "This is a test notification")
    
    battery = get_phone_battery()
    print(f"✓ Battery: {battery}%")
    
    screen = is_screen_on()
    print(f"✓ Screen on: {screen}")
