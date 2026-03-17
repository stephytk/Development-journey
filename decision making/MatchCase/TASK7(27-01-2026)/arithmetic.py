"""
3. Create a menu-driven program using match–case for basic arithmetic operations:
* 1 → Addition
* 2 → Subtraction
* 3 → Multiplication
* 4 → Division
"""

num1=int(input("enter the number1 :"))
num2=int(input("enter the number2 :"))
operation=input("Enter the operation:")

match operation:

    case "+" :print("Add : ", num1,"+",num2,"=",num1+num2)

    case "-" :print("Subtract: ", num1,"-",num2,"=",num1-num2)

    case "*" :print("Multiply : ", num1,"*",num2,"=",num1*num2)

    case "/" :print("Divide : ", num1,"/",num2,"=",num1/num2)
