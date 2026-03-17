"""
Check the character is consonant or not
"""
character=input("enter the character:") #b

VOWELS="aeiou"

if character not in VOWELS:
    print("Consonant")

else:
    print(" not consonant")