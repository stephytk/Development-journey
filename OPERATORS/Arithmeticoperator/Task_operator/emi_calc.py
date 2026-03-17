#EMI calculation
#equation=[P×R×(1+R)^N] / [(1+R)^N−1]


p=100000 #principal amount =100000
R=12 #  interest rate=12
n=12 #number of year 1(12 months)
r =R/(n*100)#  (12/12*100)=0.01 //interest rate per month
emi_amount=(p*r*(1+r)**n/((1+r)**n-1)) #emi_amount(principal*interest rate*(1+interest)** year) /((1+interest rate)** year/month-1)
print("EMI amount is RS.",emi_amount)# EMI  amount is 