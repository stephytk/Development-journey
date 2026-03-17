

fr=open("FILE OPERATIONS\\flight.txt")

flight=[]

for line in fr:

    # "1949,January,112"

    data=line.rstrip("\n").split(",") #[year,month,passengers]

    flight_data={"year":int(data[0]),"month":data[1],"passengers":int(data[2])}

    flight.append(flight_data)

print(flight)
#count
year_wise_count={}

for p in flight:
    #p={year:1950,month:jan,passengers:150}

    year=p.get("year")

    p_count=p.get("passengers")

    if year in year_wise_count:

        year_wise_count[year]+=p_count


    else:
        year_wise_count[year]=p_count



print(year_wise_count)

#sort 

# year_wise_count_sort=sorted(year_wise_count,key=year_wise_count.get)

# print(year_wise_count_sort)



flight_lst=[ [v,k] for k,v in year_wise_count.items()]

print(sorted(flight_lst))



