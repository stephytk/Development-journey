"""
create a list of even numbers form range of 20 to 50
"""

even=[i for i in range(20,51) if i%2==0 ]

print(even)

words=["apple","bat","carrot","elephant","ball","red"]

new_list_words=[ wd for wd in words if len(wd)>3]

print(new_list_words)

