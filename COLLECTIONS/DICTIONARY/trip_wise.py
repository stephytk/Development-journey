"""

"rahul":100
"""

manali={"rahul":300,"raj":1000,"Kiran":800,"Arun":15000,"Manoj":0,"Manu":0,"Atul":500}

total_expns=0

for v in manali.values():

    total_expns+=v

print(total_expns)

individual_split=total_expns/len(manali)

print(individual_split)


spend_wise={}

for k,v in manali.items():

    payment=individual_split-v

    spend_wise[k]=payment

print(spend_wise)
