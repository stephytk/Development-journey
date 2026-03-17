"""
Uppercase and Lowercase alphabet
"""

char=input("enter character:")

asci_value=ord(char)

if asci_value in range(97,123) or asci_value in range(65,91):

    print("Its is an alphabet")

else:

    print("not an alphabet")