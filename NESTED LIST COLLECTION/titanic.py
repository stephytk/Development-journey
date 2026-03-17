"""
# q1 : number of survived passengers
# q2 : displau unique passenger class 
# q3 number of female passengers
# q4: number of survived childs 
# q5: name whose fare > 30
# q6: number survived female
# q7:top fare
# q8 : survived peoples name
# q9:survived classes
# q10:female survival rate
"""

titanic_data = [
    {"id": 1, "survived": 0, "pclass": 3, "class": "Third", "name": "Braund, Mr. Owen Harris", "sex": "male", "age": 22, "fare": 7.25},
    {"id": 2, "survived": 1, "pclass": 1, "class": "First", "name": "Cumings, Mrs. John Bradley (Florence)", "sex": "female", "age": 38, "fare": 71.28},
    {"id": 3, "survived": 1, "pclass": 3, "class": "Third", "name": "Heikkinen, Miss. Laina", "sex": "female", "age": 26, "fare": 7.92},
    {"id": 4, "survived": 1, "pclass": 1, "class": "First", "name": "Futrelle, Mrs. Jacques Heath (Lily)", "sex": "female", "age": 35, "fare": 53.10},
    {"id": 5, "survived": 0, "pclass": 3, "class": "Third", "name": "Allen, Mr. William Henry", "sex": "male", "age": 35, "fare": 8.05},
    {"id": 6, "survived": 0, "pclass": 3, "class": "Third", "name": "Moran, Mr. James", "sex": "male", "age": None, "fare": 8.45},
    {"id": 7, "survived": 0, "pclass": 1, "class": "First", "name": "McCarthy, Mr. Timothy J", "sex": "male", "age": 54, "fare": 51.86},
    {"id": 8, "survived": 0, "pclass": 3, "class": "Third", "name": "Palsson, Master. Gosta Leonard", "sex": "male", "age": 2, "fare": 21.07},
    {"id": 9, "survived": 1, "pclass": 3, "class": "Third", "name": "Johnson, Mrs. Oscar W (Elisabeth)", "sex": "female", "age": 27, "fare": 11.13},
    {"id": 10, "survived": 1, "pclass": 2, "class": "Second", "name": "Nasser, Mrs. Nicholas (Adele)", "sex": "female", "age": 14, "fare": 30.07},
    {"id": 11, "survived": 1, "pclass": 3, "class": "Third", "name": "Sandstrom, Miss. Marguerite Rut", "sex": "female", "age": 4, "fare": 16.70},
    {"id": 12, "survived": 1, "pclass": 1, "class": "First", "name": "Bonnell, Miss. Elizabeth", "sex": "female", "age": 58, "fare": 26.55},
    {"id": 13, "survived": 0, "pclass": 3, "class": "Third", "name": "Saundercock, Mr. William Henry", "sex": "male", "age": 20, "fare": 8.05},
    {"id": 14, "survived": 0, "pclass": 3, "class": "Third", "name": "Andersson, Mr. Anders Johan", "sex": "male", "age": 39, "fare": 31.27},
    {"id": 15, "survived": 0, "pclass": 3, "class": "Third", "name": "Vestrom, Miss. Hulda Amanda Adolfina", "sex": "female", "age": 14, "fare": 7.85},
    {"id": 16, "survived": 1, "pclass": 2, "class": "Second", "name": "Hewlett, Mrs. (Mary D Kingcome)", "sex": "female", "age": 55, "fare": 16.00},
    {"id": 17, "survived": 0, "pclass": 2, "class": "Second", "name": "Williams, Mr. Charles Eugene", "sex": "male", "age": None, "fare": 13.00}
]

#number of survived passengers
surv_psngrs=[ di for di in titanic_data  if di.get("survived")==1]
print(f"survived Passengers = {len(surv_psngrs)}")

#display unique passenger class
passngr_class={di.get("class") for di in titanic_data}
print(passngr_class)

#number of female passengers
female_psngrs=[di for di in titanic_data if di.get("sex")=="female"]
print(len(female_psngrs))

#number of survived childs 

survived_childs=[di for di in titanic_data if  di.get("survived")==1 and di.get("age")<12 ]
print(len(survived_childs))

#whose fare>30

fare_grtr=[di.get("name") for di in titanic_data if di.get("fare")>30 ]

print (len(fare_grtr))

#q6: number survived female
survived_female=[di for di in titanic_data if di.get("survived")==1 and di.get("sex")=="female"]

print(len(survived_female))



#q7:top fare

top_fare=max([di["fare"] for di in titanic_data])

print("Top fare",top_fare)

#q8 : survived peoples name

survived_name=[di.get("name") for di in titanic_data if di.get("survived")==1]

print(survived_name)

 #q9:survived classes

survived_classes=[di.get("pclass") for di in titanic_data if di.get("survived")==1]

print(survived_classes)

# survived_female=[di for di in titanic_data if di.get("sex")=="female" and di.get("survived")==1]
survived_female=[di for di in titanic_data if di.get("survived")==1 and di.get("sex")=="female"]

print(len(survived_female)/len(survived_female)*100)

