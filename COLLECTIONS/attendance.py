"""
Attendance from Sunday to saturday
"""

attendance_log=['H','P','P','P','P','P','L','H']
                #  0   1   2   3   4   5    6  7


#THU=>HOLIDAY

attendance_log[4]="H"

print(attendance_log)

    

for at in attendance_log:#using algorithm index
    
    print(at)



holiday_count=0

present_count=0

for att in attendance_log:

    if att=='H':

        holiday_count+=1

    elif att=='P':

        present_count+=1


print("Holiday count",holiday_count)

print("Present  count",present_count)


