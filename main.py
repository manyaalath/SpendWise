"""
Expense Agent - Main Entry Point
This is the main program that ties all modules together.

Run this file to simulate the expense tracking system:
    python main.py
"""

# Import our custom modules
from interface.mobile_actions import get_latest_sms, send_notification
from logic.expense_parser import parse_expense_amount
from logic.expense_store import add_expense
from logic.daily_tracker import get_today_total, get_today_summary
from logic.limit_checker import check_limit, get_daily_limit
from logic.streak_manager import check_and_update_streak, get_current_streak, get_best_streak


def print_banner():
    """Print a welcome banner."""
    print("\n" + "=" * 50)
    print("EXPENSE TRACKING AGENT")
    print("=" * 50 + "\n")


def print_separator():
    """Print a visual separator."""
    print("-" * 50)


def process_expense():
    """
    Main function that processes an expense.
    This simulates receiving an SMS and tracking the expense.
    """
    print_banner()
    
    # Step 1: Get latest SMS (stub - returns sample SMS)
    print("Step 1: Reading latest SMS...")
    sms_text = get_latest_sms()
    print(f"   SMS: \"{sms_text}\"")
    print()
    
    # Step 2: Parse expense amount from SMS
    print("Step 2: Parsing expense amount...")
    expense_amount = parse_expense_amount(sms_text)
    
    if expense_amount is None:
        print("   No expense found in SMS")
        print("   This might be a credit transaction or invalid SMS")
        return
    
    print(f"   Expense detected: ₹{expense_amount}")
    print()
    
    # Step 3: Store the expense
    print("Step 3: Storing expense...")
    success = add_expense(expense_amount)
    
    if not success:
        print("   Failed to store expense")
        return
    
    print(f"   Expense logged: ₹{expense_amount}")
    print()
    
    # Step 4: Calculate daily total
    print("Step 4: Calculating daily total...")
    daily_total = get_today_total()
    daily_limit = get_daily_limit()
    print(f"   Daily total: ₹{daily_total} / ₹{daily_limit}")
    print()
    
    # Step 5: Check limit warnings
    print("Step 5: Checking spending limits...")
    limit_status = check_limit(daily_total)
    
    if limit_status['exceeded']:
        print(f"   LIMIT EXCEEDED! You're at {limit_status['percentage']}% of your daily limit")
        send_notification(
            "Spending Alert",
            f"You've exceeded your daily limit! Total: ₹{daily_total}"
        )
    elif limit_status['warning']:
        print(f"   Near daily limit ({limit_status['percentage']}% used)")
        send_notification(
            "Spending Warning",
            f"You're at ₹{daily_total} / ₹{daily_limit}. Be careful!"
        )
    else:
        print(f"   Within budget ({limit_status['percentage']}% used)")
    
    print()
    
    # Step 6: Update spending streak
    print("Step 6: Updating spending streak...")
    streak_result = check_and_update_streak()
    
    current_streak = streak_result['current_streak']
    best_streak = streak_result['best_streak']
    
    if streak_result.get('already_updated'):
        print(f"   Streak already updated today")
        print(f"   Current streak: {current_streak} days (Best: {best_streak})")
    elif streak_result['streak_broken']:
        print(f"   Streak broken! Starting fresh from 0")
        print(f"   Best streak: {best_streak} days")
    else:
        print(f"   Streak: {current_streak} days (Best: {best_streak})")
        if current_streak == best_streak and current_streak > 0:
            print(f"   New personal best!")
    
    print()
    print_separator()
    
    # Print final summary
    print("\nDAILY SUMMARY")
    print_separator()
    summary = get_today_summary()
    print(f"Total Expenses: {summary['count']}")
    print(f"Total Amount:   ₹{summary['total']} / ₹{daily_limit}")
    print(f"Remaining:      ₹{daily_limit - summary['total']}")
    print(f"Streak:         {current_streak} days")
    print_separator()
    print()


def show_menu():
    """Display the main menu and handle user input."""
    while True:
        print("\n" + "=" * 50)
        print("EXPENSE AGENT MENU")
        print("=" * 50)
        print("1. Process new expense (simulate SMS)")
        print("2. View today's summary")
        print("3. View current streak")
        print("4. Change daily limit")
        print("5. Exit")
        print("=" * 50)
        
        choice = input("\nEnter your choice (1-5): ").strip()
        
        if choice == '1':
            process_expense()
        
        elif choice == '2':
            print_banner()
            summary = get_today_summary()
            limit = get_daily_limit()
            print("TODAY'S SUMMARY")
            print_separator()
            print(f"Expenses count: {summary['count']}")
            print(f"Individual amounts: {summary['expenses']}")
            print(f"Total spent: ₹{summary['total']}")
            print(f"Daily limit: ₹{limit}")
            print(f"Remaining: ₹{limit - summary['total']}")
            print_separator()
        
        elif choice == '3':
            print_banner()
            current = get_current_streak()
            best = get_best_streak()
            print("STREAK INFORMATION")
            print_separator()
            print(f"Current streak: {current} days")
            print(f"Best streak:    {best} days")
            print_separator()
        
        elif choice == '4':
            print_banner()
            current_limit = get_daily_limit()
            print(f"Current daily limit: ₹{current_limit}")
            try:
                new_limit = int(input("Enter new daily limit (₹): "))
                if new_limit > 0:
                    from logic.limit_checker import set_daily_limit
                    set_daily_limit(new_limit)
                    print(f"Daily limit updated to ₹{new_limit}")
                else:
                    print("Limit must be greater than 0")
            except ValueError:
                print("Invalid input. Please enter a number.")
        
        elif choice == '5':
            print("\nThank you for using Expense Agent!")
            print("Stay mindful of your spending!\n")
            break
        
        else:
            print("Invalid choice. Please enter 1-5.")


def main():
    """Main entry point of the application."""
    # Run menu-driven interface
    show_menu()


if __name__ == "__main__":
    main()
