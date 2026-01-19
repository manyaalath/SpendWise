"""
Demo script - Shows all features of the expense agent in action.
This script demonstrates the complete workflow with sample data.
"""

print("\n" + "=" * 70)
print(" 💰 EXPENSE AGENT - COMPLETE DEMO")
print("=" * 70)
print("\nThis demo shows all features of the expense tracking system.\n")

input("Press Enter to start the demo...")

# ============================================================================
# DEMO 1: Processing First Expense
# ============================================================================
print("\n" + "=" * 70)
print("DEMO 1: Processing an Expense")
print("=" * 70)

from interface.mobile_actions import get_latest_sms
from logic.expense_parser import parse_expense_amount
from logic.expense_store import add_expense
from logic.daily_tracker import get_today_total
from logic.limit_checker import check_limit, get_daily_limit
from logic.streak_manager import check_and_update_streak

# Simulate receiving SMS
print("\n📱 Simulating incoming SMS...")
sms = get_latest_sms()
print(f"   SMS Received: \"{sms}\"")

# Parse the amount
print("\n🔍 Parsing expense amount...")
amount = parse_expense_amount(sms)
if amount:
    print(f"   ✓ Detected expense: ₹{amount}")
else:
    print("   ✗ No expense detected")
    exit()

# Store the expense
print("\n💾 Storing expense in database...")
add_expense(amount)
print(f"   ✓ Expense of ₹{amount} saved to expenses.json")

# Calculate daily total
print("\n📊 Calculating daily total...")
daily_total = get_today_total()
daily_limit = get_daily_limit()
print(f"   Daily spending: ₹{daily_total} / ₹{daily_limit}")

# Check limit
print("\n⚠️  Checking spending limits...")
limit_status = check_limit(daily_total)
if limit_status['exceeded']:
    print(f"   🚨 EXCEEDED! You're at {limit_status['percentage']}% of limit")
elif limit_status['warning']:
    print(f"   ⚠️  WARNING! You're at {limit_status['percentage']}% of limit")
else:
    print(f"   ✓ Within budget ({limit_status['percentage']}% used)")

# Update streak
print("\n🔥 Updating spending streak...")
streak_result = check_and_update_streak()
print(f"   Current streak: {streak_result['current_streak']} days")
print(f"   Best streak: {streak_result['best_streak']} days")

input("\n\nPress Enter to continue to next demo...")

# ============================================================================
# DEMO 2: Adding More Expenses
# ============================================================================
print("\n" + "=" * 70)
print("DEMO 2: Adding Multiple Expenses")
print("=" * 70)

sample_expenses = [
    ("₹150 spent at Flipkart", 150),
    ("Rs.75 paid to Spotify", 75),
    ("INR 200 spent via UPI to Zomato", 200),
]

print("\nAdding 3 more expenses to test the limit warning system...\n")

for sms_text, expected_amount in sample_expenses:
    print(f"📱 SMS: \"{sms_text}\"")
    amount = parse_expense_amount(sms_text)
    if amount:
        add_expense(amount)
        print(f"   ✓ Added ₹{amount}")
    else:
        print(f"   ✗ Failed to parse")
    print()

input("Press Enter to view summary...")

# ============================================================================
# DEMO 3: Viewing Summary
# ============================================================================
print("\n" + "=" * 70)
print("DEMO 3: Today's Summary")
print("=" * 70)

from logic.daily_tracker import get_today_summary

summary = get_today_summary()
daily_total = summary['total']
daily_limit = get_daily_limit()

print("\n📈 DAILY SUMMARY")
print("-" * 70)
print(f"Number of expenses:  {summary['count']}")
print(f"Individual amounts:  {summary['expenses']}")
print(f"Total spent:         ₹{daily_total}")
print(f"Daily limit:         ₹{daily_limit}")
print(f"Remaining budget:    ₹{daily_limit - daily_total}")
print("-" * 70)

# Check if we're near or over limit
limit_status = check_limit(daily_total)
print(f"\n💡 Status: ", end="")
if limit_status['exceeded']:
    print(f"⚠️  OVER LIMIT by ₹{daily_total - daily_limit}!")
elif limit_status['warning']:
    print(f"⚠️  Near limit ({limit_status['percentage']}% used)")
else:
    print(f"✓ Good! Only {limit_status['percentage']}% of budget used")

input("\n\nPress Enter to continue...")

# ============================================================================
# DEMO 4: Streak Information
# ============================================================================
print("\n" + "=" * 70)
print("DEMO 4: Spending Streak")
print("=" * 70)

from logic.streak_manager import get_current_streak, get_best_streak

current = get_current_streak()
best = get_best_streak()

print("\n🔥 STREAK INFORMATION")
print("-" * 70)
print(f"Current streak:  {current} days")
print(f"Best streak:     {best} days")
print("-" * 70)

if daily_total > daily_limit:
    print("\n⚠️  Your streak will break today because you exceeded the limit!")
    print("   Try to stay under ₹500 tomorrow to start a new streak.")
else:
    print(f"\n✓ Great job! Keep spending under ₹{daily_limit} to maintain your streak!")

input("\n\nPress Enter to continue...")

# ============================================================================
# DEMO 5: Changing Daily Limit
# ============================================================================
print("\n" + "=" * 70)
print("DEMO 5: Changing Daily Limit")
print("=" * 70)

from logic.limit_checker import set_daily_limit

current_limit = get_daily_limit()
print(f"\nCurrent daily limit: ₹{current_limit}")

# Let's increase the limit to avoid exceeding
new_limit = 800
print(f"Setting new limit to: ₹{new_limit}")

set_daily_limit(new_limit)
print(f"✓ Daily limit updated!")

# Re-check status with new limit
print(f"\nRechecking with new limit...")
limit_status = check_limit(daily_total)
print(f"Total: ₹{daily_total} / ₹{new_limit}")
print(f"Usage: {limit_status['percentage']}%")
print(f"Status: ", end="")
if limit_status['warning']:
    print("⚠️  Near limit")
else:
    print("✓ Within budget")

input("\n\nPress Enter to continue...")

# ============================================================================
# DEMO 6: File Storage Verification
# ============================================================================
print("\n" + "=" * 70)
print("DEMO 6: Data Files")
print("=" * 70)

import json
import os
from logic.expense_store import get_data_dir

data_dir = get_data_dir()

print(f"\nAll data is stored in: {data_dir}\n")

# Show expenses.json
expenses_file = os.path.join(data_dir, 'expenses.json')
if os.path.exists(expenses_file):
    with open(expenses_file, 'r') as f:
        expenses_data = json.load(f)
    print("📄 expenses.json:")
    print(json.dumps(expenses_data, indent=2))

# Show config.json
config_file = os.path.join(data_dir, 'config.json')
if os.path.exists(config_file):
    with open(config_file, 'r') as f:
        config_data = json.load(f)
    print("\n📄 config.json:")
    print(json.dumps(config_data, indent=2))

# Show streak.json
streak_file = os.path.join(data_dir, 'streak.json')
if os.path.exists(streak_file):
    with open(streak_file, 'r') as f:
        streak_data = json.load(f)
    print("\n📄 streak.json:")
    print(json.dumps(streak_data, indent=2))

# ============================================================================
# FINAL SUMMARY
# ============================================================================
print("\n" + "=" * 70)
print(" ✓ DEMO COMPLETE!")
print("=" * 70)

print("""
What you just saw:

✓ SMS parsing from multiple formats (₹, Rs., INR)
✓ Automatic expense storage in JSON files
✓ Daily spending calculations
✓ Limit warnings at 80% threshold
✓ Spending streak tracking
✓ Configurable daily limits
✓ Persistent data storage

All features are working perfectly!

To use the interactive menu:
    python main.py

To run automated tests:
    python test_system.py

Thank you for watching the demo! 🚀
""")

print("=" * 70 + "\n")
