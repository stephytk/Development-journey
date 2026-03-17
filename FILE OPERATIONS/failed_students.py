
fr1=open("FILE OPERATIONS\\all_students.txt","r")

fr2=open("FILE OPERATIONS\\passed_students.txt","r")

all_student_list=[line.rstrip("\n") for line in fr1]

passed_student_list=[line.rstrip("\n") for line in fr2]

print("all",all_student_list)

print("Passed students",passed_student_list)

failed_student_list=set(all_student_list).difference(passed_student_list)

print("Failed students",failed_student_list)




