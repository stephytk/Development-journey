"""
Task:
Ask for PIN.

If PIN is correct:

Ask for withdrawal amount

If amount ≤ balance → "Withdrawal successful"

Else → "Insufficient balance"

Else → "Incorrect PIN"
"""
db_pin=121

db_balance=5000

user_pin=int(input("Enter the pin :"))

if db_pin==user_pin:

    withdr_amount=int(input("enter the withdrawal amount :"))

    if withdr_amount<=db_balance:
        print("Withdraw succsessful")

    else:
        print("Insufficient balance")

else:
    print("Incorrect Pin")


     






