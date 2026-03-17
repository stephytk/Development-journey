"""
Write a program using match–case to print the number of days in a month based on the month name.

"""

month_name=(input("Enter the month :"))

match month_name:

    case "January"| "March"| "May" |"July"| "August "| "October" |"December":
        print("31 days")

    case "February":

        print("28/29 days")

    case "April" | "June" |"September" |"November" :

        print("30 days")

    case _:

        print("Invalid month")




   
    # case "Jan" :print("31")

    # case "Feb" :print("28")

    # case "Mar" :print("31")

    # case "Apr" :print("30")

    # case "May" :print("31")

    # case "Jun" :print("30")

    # case "Jul" :print("31")

    # case "Aug" :print("31")

    # case "Sep" :print("30")

    # case "Oct" :print("31")

    # case "Nov" :print("30")
    
    # case "Dec" :print("31")

    # case _: print("Invalid month name")




     

