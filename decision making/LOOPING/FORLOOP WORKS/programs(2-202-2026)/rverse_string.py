"""
Reverse string
"""

word=input("Enter the word :")

result=""

word_length=len(word)-1

for i in range(word_length,-1,-1):

    result=result+word[i]

print(result)


