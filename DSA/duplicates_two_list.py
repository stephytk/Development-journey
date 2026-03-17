"""
"""

lst1=[10,11,12,13,14]

lst2=[8,11,14,15,16]

for num in lst1:

    if num in lst2:

        print(num)


#method 2

lst_set1=set(lst1)

lst_set2=set(lst2)

new_set=lst_set1.intersection(lst_set2)

print(new_set)
   

#method 3
lst1=[10,11,12,13,14]

lst2=[8,11,14,15,16]

lst1.sort()

lst2.sort()
