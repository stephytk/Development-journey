from csv import DictReader

fr=open("FILE OPERATIONS\\CSV\\tips.csv")

#csv =>list_of_dict[csv.py=>DictReader]

data=list(DictReader(fr))

print(data)

datawise_summary ={}

for d in data:

   tip=float(d.get("tip"))

   day= d.get("day")

   if day in datawise_summary:

    datawise_summary[day]+=tip


   else:
      datawise_summary[day]=tip

print(datawise_summary)

#day with highest revenue


highest_revenue={}

for d in data:
  
  day=d.get("day")

  total_bill=float(d.get("total_bill"))

  if day in highest_revenue:

        highest_revenue[day]+=total_bill

  else:
     
     highest_revenue[day]=total_bill

print(highest_revenue)

#male or female(highest tip)

highest_tip={}

for d in data:
   
      tip=float(d.get("tip"))

      gender=d.get("sex")

      if gender in highest_tip:
    
            highest_tip[gender]+= tip
      else:
            highest_tip[gender]=tip

print(highest_tip)
             
#value with key

high_tip=[[v,k] for k,v in highest_tip.items()]

print(max(high_tip))




    
     
  

       




