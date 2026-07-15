product_name = input("Enter the product name: ")
quantity = int(input("Enter the quantity: "))
unit_price = float(input("Enter the unit price: "))

total_cost = quantity * unit_price

print("\n--- Receipt ---")
print(f"Product: {product_name}")
print(f"Quantity: {quantity}")
print(f"Unit Price: ₱{unit_price:.2f}")
print(f"Total Cost: ₱{total_cost:.2f}")