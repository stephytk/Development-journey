"""

 cube of a number=123 
"""

number=123 #123
sum=0 #0

while(number!=0): #123!=0

    last_digit=number%10  #123%10=>3

    cube=last_digit**3 #cube=3**3

    sum=sum+cube #sum=0+27
  
    number= number//10
print(sum)

     