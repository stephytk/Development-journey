"""
Read a num
Display FIZZ  if num/3
Display BUZZ  if num/5
Display FIZZBUZZ  if num/15

"""
number=int(input("Enter the number:"))
if number%15==0:
    print("FIZZBUZZ")
elif number%5==0:
    print("BUZZ")
elif number%3==0:
    print("FIZZ")
else:
    print("INVALID..")