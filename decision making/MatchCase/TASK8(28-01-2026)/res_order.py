"""
Restaurant Order System
------------------------------------
Task:
- Ask for table number

If table exists:
    - Ask for food availability
    - If food available:
        "Order placed"
    - Else:
        "Item out of stock"
Else:
    "Invalid table number"

"""
tab_no=8

table_num=int(input("Enter the table number :"))

if table_num ==tab_no:
    food_aval=int(input("Enter the food availabilty :"))

    if food_aval>0:
        print("Order Placed")
    else:
        print("Item out of stock")

else:
    print("invalid table number")