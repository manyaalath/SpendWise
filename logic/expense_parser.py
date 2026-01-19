"""
Expense Parser Module
Extracts expense amounts from bank SMS text messages.
"""

import re


def parse_expense_amount(sms_text):
    """
    Parse expense amount from SMS text.
    
    Args:
        sms_text (str): Raw SMS text from bank
        
    Returns:
        int or None: Extracted expense amount, or None if not found
        
    Examples:
        "₹299 debited from your account" -> 299
        "Rs.120 spent via UPI" -> 120
        "Your account credited with ₹500" -> None (ignore credits)
    """
    # Return None if input is empty or None
    if not sms_text:
        return None
    
    # Convert to lowercase for easier pattern matching
    text_lower = sms_text.lower()
    
    # Ignore credit transactions (we only want debits/expenses)
    if 'credit' in text_lower or 'received' in text_lower or 'deposited' in text_lower:
        return None
    
    # Look for debit/expense indicators
    is_expense = any(keyword in text_lower for keyword in 
                     ['debit', 'spent', 'paid', 'purchase', 'withdrawn'])
    
    if not is_expense:
        return None
    
    # Pattern to match amounts with ₹ or Rs. or Rs or INR
    # This will match: ₹299, Rs.120, Rs 150, INR 200
    patterns = [
        r'₹\s*(\d+)',           # ₹299 or ₹ 299
        r'Rs\.?\s*(\d+)',       # Rs.120 or Rs 120
        r'INR\s*(\d+)',         # INR 200
    ]
    
    # Try each pattern
    for pattern in patterns:
        match = re.search(pattern, sms_text)
        if match:
            try:
                amount = int(match.group(1))
                return amount
            except ValueError:
                continue
    
    # If no pattern matched, return None
    return None


# Test function for development
def _test_parser():
    """Internal test function to verify parser works correctly."""
    test_cases = [
        ("₹299 debited from your account", 299),
        ("Rs.120 spent via UPI", 120),
        ("Rs 150 spent at Amazon", 150),
        ("INR 200 paid to Zomato", 200),
        ("Your account credited with ₹500", None),
        ("Random text without amount", None),
        ("", None),
    ]
    
    print("Testing expense parser...")
    for text, expected in test_cases:
        result = parse_expense_amount(text)
        status = "PASSED" if result == expected else "FAILED"
        print(f"{status} Input: '{text}' -> Expected: {expected}, Got: {result}")


if __name__ == "__main__":
    _test_parser()
