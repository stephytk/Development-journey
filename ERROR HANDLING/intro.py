"""
Error handling

Blocks

* try: => Doubtful code
* except: =>handling code

"""

lst=[10,11,12,13,14]


index=int(input("Enter the index pos"))

try:

    print(lst[index])

except Exception as e:

    print(e)

finally:
    
    print("database commit")

    print("file write")
