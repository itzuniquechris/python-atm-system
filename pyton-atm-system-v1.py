balance = 1000.00
correct_pin = "1234"

print("====================================")
print("  WELCOME TO PYTHON BOOTCAMP ATM    ")
print("====================================")

while True:
  pin = int(input("\nEnter your 4-digit PIN: "))

  if pin != correct_pin:
    print("[!] Incorrect PIN. Please try again.")
  else:
    print("[✓] PIN Verified. Welcome, User!")
    break

while True:
  print("\n---------- MAIN MENU ----------")
  print("1. Check Balance")
  print("2. Deposit Money")
  print("3. Withdraw Money")
  print("4. Exit")

  option = input("Choose an option: ")

  if option == "1":
    print(f"[i] Your current balance is: ${balance:.2f}")
  
  elif option == "2":
    amount = input("Enter amount to deposit: ")

    if amount.isalpha():
      print("[!] Invalid input. Please enter numbers only.")
      continue

    else:
      print(f"[✓] ${amount} deposited successfully.")
      balance += float(amount)
      print(f"[i] New Balance: $ {balance:.2f}")
  
  elif option == "3":
    withdraw = float(input("Enter amount to withdraw: "))

    if withdraw > balance:
      print(f"[!] Insufficient funds! You only have ${balance:.2f}")
      continue
    else:
      print(f"[✓] Please take your cash: {withdraw:.2f}")
      balance -= withdraw
      print(f"[i] Remaining Balance: ${balance:.2f}")

  elif option == "4":
    print("\n[!] Thank you for using Python ATM. Goodbye!")
  print("====================================")
  break
