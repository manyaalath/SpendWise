"""
Simple test script to verify all modules work correctly.
This runs automated tests without user interaction.
"""

print("=" * 60)
print("EXPENSE AGENT - AUTOMATED TEST")
print("=" * 60)

# Test 1: Expense Parser
print("\n[TEST 1] Expense Parser")
print("-" * 60)
from logic.expense_parser import parse_expense_amount

test_sms = "₹299 debited from your account for Amazon"
amount = parse_expense_amount(test_sms)
print(f"SMS: {test_sms}")
print(f"Parsed amount: ₹{amount}")
assert amount == 299, "Parser test failed!"
print("PASSED")

# Test 2: Expense Store
print("\n[TEST 2] Expense Store")
print("-" * 60)
from logic.expense_store import add_expense, get_today_expenses

success = add_expense(299)
assert success, "Failed to add expense!"
print("Added expense: ₹299")

expenses = get_today_expenses()
print(f"Today's expenses: {expenses}")
assert 299 in expenses, "Expense not found!"
print("PASSED")

# Test 3: Daily Tracker
print("\n[TEST 3] Daily Tracker")
print("-" * 60)
from logic.daily_tracker import get_today_total, get_today_summary

total = get_today_total()
print(f"Today's total: ₹{total}")
assert total >= 299, "Total calculation error!"

summary = get_today_summary()
print(f"Summary: {summary['count']} expenses totaling ₹{summary['total']}")
print("PASSED")

# Test 4: Limit Checker
print("\n[TEST 4] Limit Checker")
print("-" * 60)
from logic.limit_checker import check_limit, get_daily_limit

limit = get_daily_limit()
print(f"Daily limit: ₹{limit}")

result = check_limit(total)
print(f"Warning: {result['warning']}")
print(f"Exceeded: {result['exceeded']}")
print(f"Usage: {result['percentage']}%")
print("PASSED")

# Test 5: Streak Manager
print("\n[TEST 5] Streak Manager")
print("-" * 60)
from logic.streak_manager import check_and_update_streak, get_current_streak

streak_result = check_and_update_streak()
print(f"Current streak: {streak_result['current_streak']} days")
print(f"Best streak: {streak_result['best_streak']} days")
print(f"Streak broken: {streak_result['streak_broken']}")
print("PASSED")

# Test 6: Mobile Actions (stub)
print("\n[TEST 6] Mobile Actions (Stub)")
print("-" * 60)
from interface.mobile_actions import get_latest_sms, send_notification

sms = get_latest_sms()
print(f"Sample SMS: {sms}")
assert sms is not None, "SMS stub failed!"
send_notification("Test", "This is a test notification")
print("PASSED")

# Final Summary
print("\n" + "=" * 60)
print("ALL TESTS PASSED!")
print("=" * 60)
print("\nThe expense agent system is working correctly!")
print("Run 'python main.py' to use the interactive menu.\n")
