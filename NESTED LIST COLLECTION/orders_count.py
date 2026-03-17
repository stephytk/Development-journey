

orders=["tea","coffee","idly","coffee","tea","dosa","tea","coffee"]

order_count={o:orders.count(o) for o in orders}

print(order_count)


#without comprehension
order_count={}

for o in orders:

    order_count[o]=orders.count(o)

print(order_count)