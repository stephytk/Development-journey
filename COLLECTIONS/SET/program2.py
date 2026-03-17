"""
w.a.p to display least positive missing integer from list with +ve numbers

sample input1:
    lst=[1,2,3,5]

    o/p => 4

sample input2:
    lst=[2,3,4,5]

    o/p => 1

sample input3:
    lst=[1,2,3,4,5]
    o/p=>6
"""

lst=[1,2,3,5]

for num in range(1,6):

    if num not in lst:

        print(num)

        break

lst=[2,3,4,5]

for num in range(1,6):

    if num not in lst:

        print(num)

        break



lst=[1,2,3,4,5]

for num in range(1,7):

    if num not in lst:

        print(num)

        break





    