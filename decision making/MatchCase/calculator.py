"""

Calculator application
"""

num1=int(input("Enter number1 :"))
num2=int(input("Enter number2 :"))
operation=(input("Enter the operation :"))


match operation:
    case "+":  print(num1+num2)

    case "-":  print(num1-num2)

    case "*":  print(num1*num2)

    case "/":  print(num1/num2)

    case "//": print(num1//num2)

    case "**": print(num1**num2)

    case "%":  print(num1%num2)

    case _:    print("invalid operation")

