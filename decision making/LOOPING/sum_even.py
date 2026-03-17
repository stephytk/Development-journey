"""
Sum of even numbers
"""
num=int(input("Enter the limit :"))
i=1
sum=0

while(i<=num):
    if i%2==0:
        
        sum=sum+i
        
    i=i+1
print(sum)