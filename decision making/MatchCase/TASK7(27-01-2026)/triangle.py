"""
Write a program using match–case to print the type of triangle based on a given input:
* "e" → Equilateral
* "i" → Isosceles
* "s" → Scalene


"""
typ_of_triangle=input("Enter the type of triangle :")

match typ_of_triangle:

    case "e": print("Equilateral")

    case "i": print("Isosceles")

    case "s":print("Scalene")

    case _:("Invalid triangle")

    