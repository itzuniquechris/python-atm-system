print("--- Welcome to Python Simple Calculator ---")

print("Available Ops: + , - , * , / , % , **")
print("Type 'exit' at any time to quit.")

while True:

    num1 = input("\nEnter first number: ")
    if num1.lower() == "exit":
        print("Shutting down calculator... Goodbye!")
        break

    if not num1.replace(".", "").isdigit():
        print("Error: '" + num1 + "' is not a valid number. Please try again.")
        continue

    num1 = float(num1)

    operator = input("Enter operator: ")
    if operator.lower() == "exit":
        print("Shutting down calculator... Goodbye!")
        break

    if operator not in ["+", "-", "*", "/", "%", "**"]:
        print("Error: '" + operator + "' is an invalid operator.")
        continue

    num2 = input("Enter second number: ")
    if num2.lower() == "exit":
        print("Shutting down calculator... Goodbye!")
        break

    if not num2.replace(".", "").isdigit():
        print("Error: '" + num2 + "' is not a valid number. Please try again.")
        continue

    num2 = float(num2)

    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        result = num1 / num2
    elif operator == "%":
        result = num1 % num2
    elif operator == "**":
        result = num1 ** num2

    print(f"> Result: {num1} {operator} {num2} = {result:.2f}")

    again = input("\nDo you want to perform another calculation? (y/n): ")
    if again.lower() != "y":
        print("Shutting down calculator... Goodbye!")
        break