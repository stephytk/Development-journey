

fr=open("FILE OPERATIONS\\vegetables.txt","r")

all_veg_list=[line.rstrip("\n") for line in fr]

all_veg_count={o:all_veg_list.count(o) for o in all_veg_list}

print(all_veg_count)












    