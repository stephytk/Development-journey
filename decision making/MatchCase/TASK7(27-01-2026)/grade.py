"""
Create a program using match–case that accepts a grade (A, B, C, D, F) and prints the result message.

"""

grade=input("Enter the Grade :")

match grade:
    
    case "A" : print("Excellent")

    case "B" : print("Good")
    
    case "C" : print("Average")

    case "D" : print("Below Average")

    case "F" : print("Fail")
