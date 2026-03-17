"""
"""

lst=[10,11,12,11,13,15,14,13]


# lst.sort()

# for prev in range(0,len(lst)-1):

#     next=prev+1

#     difference= lst[next] - lst[prev]

#     if difference==0:


#         print(lst[prev])


#Using function

def find_duplicate(arr):

    arr.sort()


    for prev in range(0,len(arr)-1):

        next=prev+1

        difference = arr[next]-arr[prev]

        if difference==0:

            print(arr[prev])

find_duplicate([11,12,11,13,14,15,13])