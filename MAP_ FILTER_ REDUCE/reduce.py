"""
"""

from functools import reduce

arr=[10,11,12,13,14,15,16]

result = reduce(lambda n1,n2:n1*n2,arr)

print(result)
