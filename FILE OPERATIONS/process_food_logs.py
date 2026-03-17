

fr=open("FILE OPERATIONS\\food_logs.txt")

food_logs=[]

for line in fr:

    #"1,break_fast,idly,175,11-1-2025,hari"

    data=line.rstrip("\n").split(",") #[id,meal_type,name,calorie,date,owner]

    fd_log={"id":data[0],"meal_type":data[1],"name":data[2],"calorie":float(data[3]),"date":data[4],"owner":data[5]}

    food_logs.append(fd_log)



print(food_logs)


total_cal=sum([tp["calorie"] for tp in food_logs])

print(total_cal)










