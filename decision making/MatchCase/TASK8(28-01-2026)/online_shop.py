"""
3. Online Shopping – Coupon Check
------------------------------------
Task:
- Ask for coupon code

If coupon code is valid:
    - Ask for cart amount
    - If amount ≥ 1000:
        "Coupon applied"
    - Else:
        "Minimum purchase not met"
Else:
    "Invalid coupon"

"""
c_code=12356
coupon_code=int(input("Enter the coupon code :"))

if c_code==coupon_code:
    cart_amount=int(input("Enter the amount :"))
    if cart_amount>=1000:
        print("coupon applied")
    else:
        print("Minimum purchase not met")
else:
    print("Invalid coupon")