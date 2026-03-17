"""
*args => recieve number of parameter as tuple
"""

def add(*args):

    return sum(args)

print(add(10,20))

print(add(10,20,30))

print(add(10,20,30,40,50))



def largest_num(*args):

    return max(args)

print(largest_num(10,40))
print(largest_num(10,40,70))


def count_even(*args:tuple):

    # count = 0

    # for num in args:

    #     if num%2==0:
         
    #      count=count+1

    # return count

    evens=[num for num in args if num%2==0]

    return len(evens)

print(count_even(10,11,12,13))

print(count_even(10,11,12,13,14))


def count_odd(*args:tuple):

    odds =[num for num in args if num%2!=0]

    return len(odds)


print(count_odd(10,11,12,13))

print(count_odd(14,15,16,17,18,19))







