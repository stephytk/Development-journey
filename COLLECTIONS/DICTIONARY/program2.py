"""
create a dictionary to store student details
"""

student_details={"id":10,"name":"Rahul","course":"BCA","marks":450}

print(student_details["name"])

#update marks by adding 5 bonus marks

student_details["marks"]+=5

print(student_details)

#add a new key grade

student_details["grade"]="A grade"

print(student_details)

#chk addtendance key exixt  or not

if "attendance" in student_details:

    print("yes")
else:
    print("no")

