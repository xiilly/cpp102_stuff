daily_allowance = float(input("Enter your daily allowance: "))
transportation_expense = float(input("Enter your transportation expense: "))
food_expense = float(input("Enter your food expense: "))

total_expenses = transportation_expense + food_expense
remaining_allowance = daily_allowance - total_expenses
is_within_allowance = total_expenses <= daily_allowance

print("\n--- Daily Allowance Summary ---")
print(f"Daily Allowance: ₱{daily_allowance:.2f}")
print(f"Total Expenses: ₱{total_expenses:.2f}")
print(f"Remaining Allowance: ₱{remaining_allowance:.2f}")
print(f"Within Allowance: {is_within_allowance}")