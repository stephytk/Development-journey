"""
Create a program that:
Takes student name
Takes course fee
Takes amount paid
Raise error if:
Fee is negative
Paid amount is negative
Paid amount is greater than fee
Handle invalid input
Always print "Registration Process Finished" using finally
"""
try:
    stud_name=input("Enter the name") #doubtful code

    course_fee=int(input("enter the course fee"))

    amnt_paid=int(input("Enter the amount paid"))

    if course_fee<0:

        raise Exception("fee is negative") #raise custom error
    if amnt_paid<0:
         
        raise Exception("paid amount is negative")
    
    if amnt_paid > course_fee:

        raise Exception("paid amount is greater than fee")
    
except Exception as e: #handling code

    print(e)
finally:

    print("Registration Process Finished")













