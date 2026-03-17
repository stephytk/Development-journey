"""
Write a program that takes a traffic light color as input and prints the corresponding action using match–case
"""

traffic_light=input("Enter the traffic light color :")

match traffic_light:

    case    "green" :   print("Go")

    case    "yellow":   print("Wait")

    case    "red"   :   print("Stop")

    case _: ("Invalid signal")



