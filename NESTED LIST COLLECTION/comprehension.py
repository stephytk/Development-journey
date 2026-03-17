"""
Comprehension => Easy way for creating a sequence from another sequence

syntax: [left middle right]
"""

arr=[10,12,13,14,15]

squares=[num** 2 for num in arr]

     #   return   iteration

print(squares)

cubes=[ num **3 for num in  arr]

print(cubes)


add=[num+ 10 for num in arr]

print(add)