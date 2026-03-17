""""
"""

def max_two(n1,n2):

    result=1

    if n1 > n2:

        result = n1
    else:

        result = n2

    return result

assert max_two(10,20)==20,"Test case1 failed"

assert max_two(-10,5)==5,"Test case2 failed"

print("Code accepted...")

