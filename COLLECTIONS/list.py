"""
List program

SYNTAX: lis[index]=value
"""

food_logs=["tea","idly","sambar","tea","rice"]
        #   0     1       2        3     4

food_logs[3]="Coffee" #update

# print(food_logs)


#display value in 4th index
# print(food_logs[4])

# print(food_logs[0])

# print(food_logs[1])

# print(food_logs[2])

# print(food_logs[3])



# # using for loop with index

# for i in range(0,5):

#     print(food_logs[i])


#using algorithm index(direct access elements)

for f in food_logs:  #take each item from the list ,store in the variable 'f' 
    
    print(f) #then print one by one