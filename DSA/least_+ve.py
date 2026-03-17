"""

Least positive integer with positive
"""

lst=[1,2,3,5]

length=len(lst)

for num in range(1,length+1):

    if num not in lst:

        print(num)

        break
        


#another method

lst=[1,2,3,5]

lst.sort()

prev=0




lst=[2,3,4,5]

length=len(lst)

for  num in range(1,length+1):

    if num not in lst:

        print(num)

        break

lst=[1,2,3,4,5]

length=len(lst)

for num in range(1,length+2):

    if num not in lst:

        print(num)

        break



    