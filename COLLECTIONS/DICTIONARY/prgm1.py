"""
"""

product={"id":1234,"title":"oreo","price":50,"aval_qty":60}
print(product)

#update aval_qty as 70

product["aval_qty"]+=10

print(product)

#add code "sku12"

product["code"]="sku12"

print(product)

#check key exist or not

if "offer" in product:

    print("yes")

else:

    print("no")

