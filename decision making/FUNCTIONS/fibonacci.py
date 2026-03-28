

def is_fibonacci(number):

    is_fibo= False

    prev=0
    curr=1
    next=prev+curr

    while(next<=number):

        next=prev+curr

        prev=curr

        curr=next

        if next==number:

            is_fibo=True

            break

    return is_fibo

print(is_fibonacci(8))
        
         
    
    



    

  




