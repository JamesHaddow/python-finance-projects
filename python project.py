print("Welcome to the Investment Return Calculator!")

# Get user input
principal = float(input("Enter the initial investment (£): "))
rate = float(input("Enter the annual interest rate (%): "))
years = int(input("Enter the number of years: "))
contribution = float(input("Enter monthly contribution (£, 0 if none): "))

# Calculate simple interest
simple = principal * (1 + rate/100 * years) + contribution * 12 * years

# Calculate compound interest
compound = principal
for year in range(1, years + 1):
    compound = compound * (1 + rate/100)
    compound += contribution * 12  # Add contributions at the end of each year

# Display results
print("\n--- Investment Summary ---")
print(f"Future value with simple interest: £{simple:,.2f}")
print(f"Future value with compound interest: £{compound:,.2f}")



