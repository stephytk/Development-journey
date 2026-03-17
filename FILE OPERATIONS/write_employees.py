
"""
write  in file operation
"""

employees=["Hari","Rahul","Arun","Vinu"]

fw=open("FILE OPERATIONS\\employees.txt","w")


for e in employees:

    fw.write(e+"\n")

    print("completed")
    
fw=open("FILE OPERATIONS\\employees.txt","a")

for e in employees:

    fw.write(e+"\n")

    print("completed")

    