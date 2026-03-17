"""
Movie Ticket Booking
------------------------------------
Task:
- Ask for age

If age ≥ 18:
    - Ask for seat availability
    - If seats available:
        "Ticket booked"
    - Else:
        "House full"
Else:
    "Not eligible to watch the movie"t
"""




age=int(input("Enter the age :"))


if age>=18:
    seat_avail=int(input("Enter the seat availability :"))

    if seat_avail>0:

        print("ticket booked")

    else:
       
       print ("Housefull")
else:
   print ("Not eligible to watch the movie")
