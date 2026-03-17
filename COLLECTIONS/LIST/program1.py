"""
Docstring for COLLECTIONS.LIST.program1
"""

numbers=[-1,-1,10,11,12,13,-13,4,5]

postv_list=[]

neg_list=[]

for num in numbers:

    if num>0:

        postv_list.append(num)

    elif num<0:

        neg_list.append(num)

print("Psitive List", postv_list)

print("Negative List", neg_list)