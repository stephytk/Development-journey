"""
Read two values attendance and mark and print the result of attendance >= 75 and mark >= 40.
"""

attendance=int(input(" enter the attendance of students :")) #55
mark=int(input("enter the marks "))#40

if(attendance>=75 and mark>=40):#55>=75 False and 40>=40 True
    print("Attendance is greater than or equal to 75 and mark is greater than 40")

else:
    print("not greater than 75 and  40") #Not greater than 75 and 40   
