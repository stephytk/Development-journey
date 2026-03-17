"""
Docstring for COLLECTIONS.LIST.program3
"""

stock_list1=[10,11,12,13,14,15]

stock_list2=[20,21,22,23,24,25]


 
update_stk_list=[]

stock_list1.extend(stock_list2)

for num in stock_list1:

    update_stk_list.append(num +5)

print(update_stk_list)

