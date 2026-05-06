import math

print("--- Energy Auditor ---")
appliance = input("Appliance Name: ")
watts = int(input("Power (Watts): "))
hours = float(input("Hours per day: "))
price = float(input("Price per kWh: "))

daily_kwh = (watts * hours) / 1000
monthly_cost = daily_kwh * 30 * price

print("\n--- Results ---")

print(f"The {appliance} costs ${monthly_cost:.2f} per month.")
print(f"Safety Buffer Estimate: ${math.ceil(monthly_cost)}")

if monthly_cost > 50:
    print("High energy usage detected!")
elif monthly_cost < 5:
    print("You qualify for the Eco-Discount!")
else:
    print("Usage is within normal range.")
