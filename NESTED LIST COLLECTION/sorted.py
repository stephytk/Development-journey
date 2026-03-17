"""

Sort dictionary with respect to key or value
"""

orders={"tea":15,"coffee":21,"dosa":34,"rice":67}

order_lst=[ [v,k] for k,v in orders.items()]

print(sorted(order_lst,reverse=True))