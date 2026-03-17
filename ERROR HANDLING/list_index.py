

"""
Error handling

Blocks

* try: => Doubtful code
* except: =>handling code

"""

lst=[10,11,12,13,14]


index=int(input("Enter the index"))

try:

    print(lst[index])

except Exception as e:

    # index=int(input("Enter the index"))

    # print(lst[index])

    print(e)

finally:
    
    print("file operation.....")

    print("db commit....")
