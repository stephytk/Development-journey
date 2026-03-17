"""

"""

sales_report={"sun":23000,"mon":16000,"tue":18000,"wed":15000,"thu":19000,"fri":19000,"sat":20000}
total_sale=0

for sr in sales_report:

    print(sr,sales_report[sr])

    total=sales_report[sr]
    
    total_sale=total_sale+total

print(total_sale)

avg_sales=total_sale/len(sales_report)

for sr in sales_report:


    if sales_report[sr] < avg_sales:    

        print(sr,sales_report[sr])



